# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines
# pylint: disable=unused-argument
# pylint: disable=line-too-long

import ctypes
import json
import os
import platform
import subprocess
import time
import urllib.request
from zipfile import ZipFile
import shutil
import requests
from knack.util import CLIError
from azure.cli.core.azclierror import CLIInternalError
from azure.cli.core.azclierror import FileOperationError
from azure.cli.core.azclierror import InvalidArgumentValueError


# -----------------------------------------------------------------------------------------------------------------
# Common helper function to validate if the commands are running on Windows.
# -----------------------------------------------------------------------------------------------------------------
def validate_os_env():

    if 'Windows' not in platform.system():
        raise CLIInternalError("This command cannot be run in non-windows environment. Please run this command in Windows environment")


# -----------------------------------------------------------------------------------------------------------------
# Assessment helper function to test whether the given config_file_path is valid and has valid action specified.
# -----------------------------------------------------------------------------------------------------------------
def validate_config_file_path(path, action):

    if not os.path.exists(path):
        raise InvalidArgumentValueError(f'Invalid config file path: {path}. Please provide a valid config file path.')

    # JSON file read and validation of value in action
    with open(path, "r", encoding=None) as f:
        configJson = json.loads(f.read())
    try:
        if not configJson['action'].strip().lower() == action:
            raise FileOperationError(f"The desired action in config file was invalid. Please use \"{action}\" for action property in config file")
    except KeyError as e:
        raise FileOperationError("Invalid schema of config file. Please ensure that this is a properly formatted config file.") from e


# -----------------------------------------------------------------------------------------------------------------
# Helper function to test whether the path exists.
# -----------------------------------------------------------------------------------------------------------------
def test_path_exist(path):

    if not os.path.exists(path):
        raise InvalidArgumentValueError(f'Invalid config file path: {path}. Please provide a valid config file path.')


# -----------------------------------------------------------------------------------------------------------------
# Assessment helper function to do console app setup (mkdir, download and extract)
# -----------------------------------------------------------------------------------------------------------------
def console_app_setup():

    validate_os_env()

    defaultOutputFolder = get_default_output_folder()

    # Assigning base folder path
    baseFolder = os.path.join(defaultOutputFolder, "Downloads")
    exePath = os.path.join(baseFolder, "SqlAssessment.Console.csproj", "SqlAssessment.exe")

    # Creating base folder structure
    create_dir_path(baseFolder)
    # check and download console app
    check_and_download_console_app(exePath, baseFolder)

    return defaultOutputFolder, exePath


# -----------------------------------------------------------------------------------------------------------------
# LoginMigration helper function to do console app setup (mkdir, download and extract)
# -----------------------------------------------------------------------------------------------------------------
def loginMigration_console_app_setup():
    validate_os_env()

    # Create downloads directory if it doesn't already exists
    default_output_folder = get_loginMigration_default_output_folder()
    downloads_folder = os.path.join(default_output_folder, "Downloads")
    os.makedirs(downloads_folder, exist_ok=True)

    # Delete the old Login console app
    login_migration_console_zip = os.path.join(downloads_folder, "LoginsMigration.zip")
    login_migration_console_csproj = os.path.join(downloads_folder, "Logins.Console.csproj")
    login_migration_version_file = os.path.join(downloads_folder, "loginconsoleappversion.json")
    if os.path.exists(login_migration_console_zip):
        os.remove(login_migration_console_zip)
    if os.path.exists(login_migration_console_csproj):
        shutil.rmtree(login_migration_console_csproj)
    if os.path.exists(login_migration_version_file):
        os.remove(login_migration_version_file)

    # check and download console app
    console_app_version = check_and_download_loginMigration_console_app(downloads_folder)
    if console_app_version is None:
        raise CLIError("Connection to NuGet.org required. Please check connection and try again.")

    # Assigning base folder path\LoginsConsoleApp\console
    console_app_location = os.path.join(downloads_folder, console_app_version)

    exePath = os.path.join(console_app_location, "tools", "Microsoft.SqlServer.Migration.Logins.ConsoleApp.exe")

    return default_output_folder, exePath


# -----------------------------------------------------------------------------------------------------------------
# TdeMigration helper function to do console app setup (mkdir, download and extract)
# -----------------------------------------------------------------------------------------------------------------
def tdeMigration_console_app_setup():
    validate_os_env()

    # Create downloads directory if it doesn't already exists
    default_output_folder = get_tdeMigration_default_output_folder()
    downloads_folder = os.path.join(default_output_folder, "Downloads")
    os.makedirs(downloads_folder, exist_ok=True)

    # check and download console app
    console_app_version = check_and_download_tdeMigration_console_app(downloads_folder)
    if console_app_version is None:
        raise CLIError("Connection to NuGet.org required. Please check connection and try again.")

    # Assigning base folder path\TdeConsoleApp\console
    console_app_location = os.path.join(downloads_folder, console_app_version)

    exePath = os.path.join(console_app_location, "tools", "Microsoft.SqlServer.Migration.Tde.ConsoleApp.exe")

    return exePath


# -----------------------------------------------------------------------------------------------------------------
# SqlServerSchema helper function to do console app setup (mkdir, download and extract)
# -----------------------------------------------------------------------------------------------------------------
def sqlServerSchema_console_app_setup():

    validate_os_env()

    defaultOutputFolder = get_sqlServerSchema_default_output_folder()

    # Assigning base folder path
    baseFolder = os.path.join(defaultOutputFolder, "Downloads")
    exePath = os.path.join(baseFolder, "SchemaMigration.Console.csproj", "SqlSchemaMigration.exe")

    # Creating base folder structure
    create_dir_path(baseFolder)
    # check and download console app
    check_and_download_sqlServerSchema_console_app(exePath, baseFolder)

    return defaultOutputFolder, exePath


# -----------------------------------------------------------------------------------------------------------------
# Assessment helper function to return the default output folder path depending on OS environment.
# -----------------------------------------------------------------------------------------------------------------
def get_default_output_folder():

    osPlatform = platform.system()

    if 'Linux' in osPlatform:
        defaultOutputPath = os.path.join(os.getenv('USERPROFILE'), ".config", "Microsoft", "SqlAssessment")
    elif 'Darwin' in osPlatform:
        defaultOutputPath = os.path.join(os.getenv('USERPROFILE'), "Library", "Application Support", "Microsoft", "SqlAssessment")
    else:
        defaultOutputPath = os.path.join(os.getenv('LOCALAPPDATA'), "Microsoft", "SqlAssessment")

    return defaultOutputPath


# -----------------------------------------------------------------------------------------------------------------
# LoginMigration helper function to return the default output folder path depending on OS environment.
# -----------------------------------------------------------------------------------------------------------------
def get_loginMigration_default_output_folder():

    osPlatform = platform.system()

    if 'Linux' in osPlatform:
        defaultOutputPath = os.path.join(os.getenv('USERPROFILE'), ".config", "Microsoft", "SqlLoginMigrations")
    elif 'Darwin' in osPlatform:
        defaultOutputPath = os.path.join(os.getenv('USERPROFILE'), "Library", "Application Support", "Microsoft", "SqlLoginMigrations")
    else:
        defaultOutputPath = os.path.join(os.getenv('LOCALAPPDATA'), "Microsoft", "SqlLoginMigrations")

    return defaultOutputPath


# -----------------------------------------------------------------------------------------------------------------
# TdeMigration helper function to return the default output folder path depending on OS environment.
# -----------------------------------------------------------------------------------------------------------------
def get_tdeMigration_default_output_folder():

    osPlatform = platform.system()

    if 'Linux' in osPlatform:
        defaultOutputPath = os.path.join(os.getenv('USERPROFILE'), ".config", "Microsoft", "SqlTdeMigrations")
    elif 'Darwin' in osPlatform:
        defaultOutputPath = os.path.join(os.getenv('USERPROFILE'), "Library", "Application Support", "Microsoft", "SqlTdeMigrations")
    else:
        defaultOutputPath = os.path.join(os.getenv('LOCALAPPDATA'), "Microsoft", "SqlTdeMigrations")

    return defaultOutputPath


# -----------------------------------------------------------------------------------------------------------------
# SqlServerSchema helper function to return the default output folder path depending on OS environment.
# -----------------------------------------------------------------------------------------------------------------
def get_sqlServerSchema_default_output_folder():

    osPlatform = platform.system()

    if 'Linux' in osPlatform:
        defaultOutputPath = os.path.join(os.getenv('USERPROFILE'), ".config", "Microsoft", "SqlSchemaMigration")
    elif 'Darwin' in osPlatform:
        defaultOutputPath = os.path.join(os.getenv('USERPROFILE'), "Library", "Application Support", "Microsoft", "SqlSchemaMigration")
    else:
        defaultOutputPath = os.path.join(os.getenv('LOCALAPPDATA'), "Microsoft", "SqlSchemaMigration")

    return defaultOutputPath


# -----------------------------------------------------------------------------------------------------------------
# Assessment helper function to check if console app exists, if not download it.
# -----------------------------------------------------------------------------------------------------------------
def check_and_download_console_app(exePath, baseFolder):

    testPath = os.path.exists(exePath)

    # Downloading console app zip and extracting it
    if not testPath:
        zipSource = "https://sqlassess.blob.core.windows.net/app/SqlAssessment.zip"
        zipDestination = os.path.join(baseFolder, "SqlAssessment.zip")

        urllib.request.urlretrieve(zipSource, filename=zipDestination)
        with ZipFile(zipDestination, 'r') as zipFile:
            zipFile.extractall(path=baseFolder)


# -----------------------------------------------------------------------------------------------------------------
# LoginMigration helper function to check if console app exists, if not download it.
# -----------------------------------------------------------------------------------------------------------------
def check_and_download_loginMigration_console_app(downloads_folder):
    # Get latest LoginConsoleApp name from nuget.org
    package_id = "Microsoft.SqlServer.Migration.LoginsConsoleApp"

    latest_nuget_org_version = get_latest_nuget_org_version(package_id)
    latest_nuget_org_name_and_version = f"{package_id}.{latest_nuget_org_version}"
    latest_local_name_and_version = get_latest_local_name_and_version(downloads_folder)

    if latest_nuget_org_version is None:
        # Cannot retrieve latest version on NuGet.org, return latest local version
        return latest_local_name_and_version

    print(f"Latest Login migration console app nupkg version on Nuget.org: {package_id}.{latest_nuget_org_version}")
    if latest_local_name_and_version is not None and latest_local_name_and_version >= latest_nuget_org_name_and_version:
        # Console app is up to date, do not download update
        print(f"Installed Login migration console app nupkg version: {latest_local_name_and_version}")
        return latest_local_name_and_version

    # if cx has no consent return local version
    if latest_local_name_and_version is not None:
        print(f"Installed Login migration console app nupkg version: {latest_local_name_and_version}")
        while True:
            user_input = input("New version available. Do you want to upgrade to the new version? (yes/no): ").strip().lower()
            if user_input == "yes":
                print("Updating to the new version...")
                break
            elif user_input == "no":
                print("You chose not to upgrade.")
                return latest_local_name_and_version
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

    # Download latest version of NuGet
    latest_nuget_org_download_directory = os.path.join(downloads_folder, latest_nuget_org_name_and_version)
    os.makedirs(latest_nuget_org_download_directory, exist_ok=True)

    latest_nuget_org_download_name = f"{latest_nuget_org_download_directory}/{latest_nuget_org_name_and_version}.nupkg"
    download_url = f"https://www.nuget.org/api/v2/package/{package_id}/{latest_nuget_org_version}"

    # Extract downloaded NuGet
    print(f"Downloading and extracting the latest Login migration console app nupkg: {package_id}.{latest_nuget_org_version}")
    urllib.request.urlretrieve(download_url, filename=latest_nuget_org_download_name)
    with ZipFile(latest_nuget_org_download_name, 'r') as zipFile:
        zipFile.extractall(path=latest_nuget_org_download_directory)

    exe_path = os.path.join(latest_nuget_org_download_directory, "tools", "Microsoft.SqlServer.Migration.Logins.ConsoleApp.exe")

    if os.path.exists(exe_path):
        print("Removing all older Login migration console apps...")
        for nuget_version in os.listdir(downloads_folder):
            if nuget_version != latest_nuget_org_name_and_version:
                shutil.rmtree(os.path.join(downloads_folder, nuget_version))
    else:
        return latest_local_name_and_version

    return latest_nuget_org_name_and_version


# -----------------------------------------------------------------------------------------------------------------
# SqlServerSchema helper function to check if console app exists, if not download it.
# -----------------------------------------------------------------------------------------------------------------
def check_and_download_sqlServerSchema_console_app(exePath, baseFolder):

    testPath = os.path.exists(exePath)

    # Downloading console app zip and extracting it
    if not testPath:
        zipSource = "https://migrationapps.blob.core.windows.net/schemamigration/SqlSchemaMigration.zip"
        zipDestination = os.path.join(baseFolder, "SqlSchemaMigration.zip")

        urllib.request.urlretrieve(zipSource, filename=zipDestination)
        with ZipFile(zipDestination, 'r') as zipFile:
            zipFile.extractall(path=baseFolder)


# -----------------------------------------------------------------------------------------------------------------
# Get latest version of Console App on NuGet.org
# -----------------------------------------------------------------------------------------------------------------
def get_latest_nuget_org_version(package_id):
    # Get Nuget.org service index
    service_index_response = None
    try:
        service_index_response = requests.get("https://api.nuget.org/v3/index.json")
    except Exception:
        print("Unable to connect to NuGet.org to check for updates.")

    if (service_index_response is None or
       service_index_response.status_code != 200 or
       len(service_index_response.content) > 999999):
        return None

    json_response = json.loads(service_index_response.content)
    nuget_org_resources = json_response["resources"]

    package_base_address_type = "PackageBaseAddress/3.0.0"
    package_base_address_url = None

    for resource in nuget_org_resources:
        if resource["@type"] == package_base_address_type:
            package_base_address_url = resource["@id"]
            break

    if package_base_address_url is None:
        return None

    package_versions_response = None
    package_versions_response = requests.get(f"{package_base_address_url}{package_id.lower()}/index.json")
    if (package_versions_response.status_code != 200 or len(package_versions_response.content) > 999999):
        return None

    package_versions_json = json.loads(package_versions_response.content)
    package_versions_array = package_versions_json["versions"]
    return package_versions_array[len(package_versions_array) - 1]


# -----------------------------------------------------------------------------------------------------------------
# Get latest local version of TDE Console App
# -----------------------------------------------------------------------------------------------------------------
def get_latest_local_name_and_version(downloads_folder):
    nuget_versions = os.listdir(downloads_folder)
    if len(nuget_versions) == 0:
        return None

    nuget_versions.sort(reverse=True)
    return nuget_versions[0]


# -----------------------------------------------------------------------------------------------------------------
# TdeMigration helper function to check if console app exists, if not download it.
# -----------------------------------------------------------------------------------------------------------------
def check_and_download_tdeMigration_console_app(downloads_folder):
    # Get latest TdeConsoleApp name from nuget.org
    package_id = "Microsoft.SqlServer.Migration.TdeConsoleApp"

    latest_nuget_org_version = get_latest_nuget_org_version(package_id)
    latest_nuget_org_name_and_version = f"{package_id}.{latest_nuget_org_version}"
    latest_local_name_and_version = get_latest_local_name_and_version(downloads_folder)

    if latest_nuget_org_version is None:
        # Cannot retrieve latest version on NuGet.org, return latest local version
        return latest_local_name_and_version

    if latest_local_name_and_version is not None and latest_local_name_and_version >= latest_nuget_org_name_and_version:
        # Console app is up to date, do not download update
        return latest_local_name_and_version

    # Download latest version of NuGet
    latest_nuget_org_download_directory = os.path.join(downloads_folder, latest_nuget_org_name_and_version)
    os.makedirs(latest_nuget_org_download_directory, exist_ok=True)

    latest_nuget_org_download_name = f"{latest_nuget_org_download_directory}/{latest_nuget_org_name_and_version}.nupkg"
    download_url = f"https://www.nuget.org/api/v2/package/{package_id}/{latest_nuget_org_version}"

    # Extract downloaded NuGet
    urllib.request.urlretrieve(download_url, filename=latest_nuget_org_download_name)
    with ZipFile(latest_nuget_org_download_name, 'r') as zipFile:
        zipFile.extractall(path=latest_nuget_org_download_directory)

    exe_path = os.path.join(latest_nuget_org_download_directory, "tools", "Microsoft.SqlServer.Migration.Tde.ConsoleApp.exe")

    if os.path.exists(exe_path):
        for nuget_version in os.listdir(downloads_folder):
            if nuget_version != latest_nuget_org_name_and_version:
                shutil.rmtree(os.path.join(downloads_folder, nuget_version))

    else:
        return latest_local_name_and_version

    return latest_nuget_org_name_and_version


# -----------------------------------------------------------------------------------------------------------------
# Assessment helper function to check if baseFolder exists, if not create it.
# -----------------------------------------------------------------------------------------------------------------
def create_dir_path(baseFolder):

    if not os.path.exists(baseFolder):
        os.makedirs(baseFolder)


# -----------------------------------------------------------------------------------------------------------------
# Helper function to check IR path Extension
# -----------------------------------------------------------------------------------------------------------------
def validate_ir_extension(ir_path):

    if ir_path is not None:
        ir_extension = os.path.splitext(ir_path)[1]
        if ir_extension != ".msi":
            raise InvalidArgumentValueError("Invalid Integration Runtime Extension. Please provide a valid Integration Runtime MSI path.")


# -----------------------------------------------------------------------------------------------------------------
# Helper function to check whether the command is run as admin.
# -----------------------------------------------------------------------------------------------------------------
def is_user_admin():

    try:
        isAdmin = os.getuid() == 0
    except AttributeError:
        isAdmin = ctypes.windll.shell32.IsUserAnAdmin() != 0

    return isAdmin


# -----------------------------------------------------------------------------------------------------------------
# Helper function to validate key input.
# -----------------------------------------------------------------------------------------------------------------
def validate_input(key):
    if key == "":
        raise InvalidArgumentValueError("Failed: IR Auth key is empty. Please provide a valid auth key.")


# -----------------------------------------------------------------------------------------------------------------
# Helper function to check whether SHIR is installed or not.
# -----------------------------------------------------------------------------------------------------------------
def check_whether_gateway_installed(name):

    import winreg
    # Connecting to key in registry
    accessRegistry = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)

    # Get the path of Installed softwares
    accessKey = winreg.OpenKey(accessRegistry, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall")

    # Check if any software has name as given name
    for i in range(0, winreg.QueryInfoKey(accessKey)[0]):
        installedSoftware = winreg.EnumKey(accessKey, i)
        installedSoftwareKey = winreg.OpenKey(accessKey, installedSoftware)
        try:
            displayName = winreg.QueryValueEx(installedSoftwareKey, r"DisplayName")[0]
            if name in displayName:
                return True
        except FileNotFoundError:
            pass

    # Adding this try to look for Installed IR in Program files (Assumes the IR is always installed there) to tackle x32 bit python
    try:
        diaCmdPath = get_cmd_file_path_static()
        if os.path.exists(diaCmdPath):
            return True
        else:
            return False
    except (FileNotFoundError, IndexError):
        return False


# -----------------------------------------------------------------------------------------------------------------
# Helper function to install SHIR
# -----------------------------------------------------------------------------------------------------------------
def install_gateway(path):

    # check if gateway is installaed. If yes don't do the installation again
    if check_whether_gateway_installed("Microsoft Integration Runtime"):
        print("Microsoft Integration Runtime is already installed")
        return

    # validate path of IR MSI
    validate_ir_extension(path)

    # Check for IR path existance
    if not os.path.exists(path):
        raise InvalidArgumentValueError(f"Invalid Integration Runtime MSI path : {path}. Please provide a valid Integration Runtime MSI path")

    print("Start Integration Runtime installation")

    # Installed MSI
    installCmd = f'msiexec.exe /i "{path}" /quiet /passive'
    subprocess.call(installCmd, shell=False)
    time.sleep(30)

    print("Integration Runtime installation is complete")


# -----------------------------------------------------------------------------------------------------------------
# Helper function to register Sql Migration Service on IR
# -----------------------------------------------------------------------------------------------------------------
def register_ir(key, installed_ir_path=None):
    print(f"Start to register IR with key: {key}")

    # get SHIR installation location - using registry or user provided
    if installed_ir_path is None:
        cmdFilePath = get_cmd_file_path()
    else:
        cmdFilePath = get_cmd_file_path_from_input(installed_ir_path)

    # extract the dmgcmd.exe and RegisterIntegrationRuntime.ps1 Script path.
    directoryPath = os.path.dirname(cmdFilePath)
    parentDirPath = os.path.dirname(directoryPath)

    dmgCmdPath = os.path.join(directoryPath, "dmgcmd.exe")
    regIRScriptPath = os.path.join(parentDirPath, "PowerShellScript", "RegisterIntegrationRuntime.ps1")

    # Open Intranet Port (Necessary for Re-Register. Service has to be running for Re-Register to work.)
    portCmd = f'{dmgCmdPath} -EnableRemoteAccess 8060'

    # Register/ Re-register IR
    irCmd = f'powershell -command "& \'{regIRScriptPath}\' -gatewayKey {key}"'

    subprocess.call(portCmd, shell=False)
    subprocess.call(irCmd, shell=False)


# -----------------------------------------------------------------------------------------------------------------
# Helper function to get SHIR script path from windows registry
# -----------------------------------------------------------------------------------------------------------------
def get_cmd_file_path():

    import winreg
    try:
        # Connecting to key in registry
        accessRegistry = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)

        # Get the path of Integration Runtime
        accessKey = winreg.OpenKey(accessRegistry, r"SOFTWARE\Microsoft\DataTransfer\DataManagementGateway\ConfigurationManager")
        accessValue = winreg.QueryValueEx(accessKey, r"DiacmdPath")[0]

        return accessValue

    # Handling the case for x32 Python as x64 software like SHIR in registry are not found by x32 Python.
    except FileNotFoundError:
        try:
            diaCmdPath = get_cmd_file_path_static()
            return diaCmdPath
        except FileNotFoundError as e:
            raise FileOperationError("Failed: No installed IR found or installed IR is not present in Program Files. Please install Integration Runtime in default location and re-run this command  or use --installed-ir-path parameter to provide the installed IR location") from e
        except IndexError as e:
            raise FileOperationError("IR is not properly installed. Please re-install it and re-run this command") from e


# -----------------------------------------------------------------------------------------------------------------
# Helper function to get DiaCmdPath with Static Paths. This function assumes that IR is always installed in program files. This function is for handling the case with x32 Python
# -----------------------------------------------------------------------------------------------------------------
def get_cmd_file_path_static():

    # Base folder is taken as Program files or Program files (x86).
    baseFolderX64 = os.path.join(r"C:\Program Files", "Microsoft Integration Runtime")
    baseFolderX86 = os.path.join(r"C:\Program Files (x86)", "Microsoft Integration Runtime")
    if os.path.exists(baseFolderX86):
        baseFolder = baseFolderX86
    else:
        baseFolder = baseFolderX64

    # Add the latest version to baseFolder path.
    listDir = os.listdir(baseFolder)
    listDir.sort(reverse=True)
    versionFolder = os.path.join(baseFolder, listDir[0])

    # Create diaCmd default path and check if it is valid or not.
    diaCmdPath = os.path.join(versionFolder, "Shared", "diacmd.exe")

    if not os.path.exists(diaCmdPath):
        raise FileNotFoundError(f"The system cannot find the path specified: {diaCmdPath}")

    return diaCmdPath


# -----------------------------------------------------------------------------------------------------------------
# Helper function to get DiaCmdPath using the installed IR path user has given
# -----------------------------------------------------------------------------------------------------------------
def get_cmd_file_path_from_input(installed_ir_path):

    if not os.path.exists(installed_ir_path):
        raise FileNotFoundError(f"The system cannot find the path specified: {installed_ir_path}")

    # Create diaCmd default path and check if it is valid or not.
    diaCmdPath = os.path.join(installed_ir_path, "Shared", "diacmd.exe")

    if not os.path.exists(diaCmdPath):
        raise FileNotFoundError(f"The system cannot find the path specified: {diaCmdPath}")

    return diaCmdPath
