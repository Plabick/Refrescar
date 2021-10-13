# Refrescar
Easily enable the Windows 11 update on PCs without TPM 2.0 chips or officially supported CPUs.

Why is this needed? Microsoft artificially blocks Windows 11 from being installed on computers with AMD Ryzen first-generation CPUs and computers with TPM 1.2 chips even though Windows 11 can run well on these "incompatible" systems. Refrescar bypasses the CPU and TPM check during Windows 11 installation by safely modifying the Windows Registry.

**Refrescar works on computers running Windows 10 that are blocked from updating due to incompatible CPUs and TPM 1.2 only. Refrescar does not work on computers that are blocked from updating because they lack UEFI boot or because they contain no TPM module. Use [Microsoft's PC Health Check](https://aka.ms/GetPCHealthCheckApp) to see why your PC is blocked from updating.**
## Usage

#### Download and Run Refrescar
Download the latest version of Refrescar from (here)[https://github.com/Plabick/Refrescar/releases/]. **Run Refrescar with administrator permissions by right-clicking on Refrescar.exe and clicking `Run as administrator`.** You must run Refrescar with administrator permissions so it can modify the Windows Registry.

#### Using Refrescar
Once Refrescar is running, it's very simple to use. Simply click the only button in the window.

#### Whats next?
After running Refrescar, your PC will be able to update to Windows 11 - you'll still need to install it. 

1. Download the [Windows 11 Installation Assistant](https://www.microsoft.com/en-us/software-download/windows11) directly from Microsoft

2. Open the Assistant and select `Download Windows 11 Disk Image (ISO)`. Go through the prompts and download the ISO. 

3. When the ISO finishes downloading, right-click on it and pick `Open with`, then `Windows Explorer` to mount the virtual disc.  Then double-click the setup file to begin the installation.

4. That's it! Just be aware that Microsoft reserves the right to withhold future security updates if you install Windows 11 on an unsupported machine. 
 
## Contributing
1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin <project_name>/<location>`
5. Create the pull request.


Alternatively, see the GitHub documentation on [creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).
