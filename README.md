# Refrescar
Easily enable the Windows 11 update on PCs without TPM 2.0 chips or officaly supported CPUs.

Why is this needed? Microsoft artificaly blocks Windows 11 from being installed on computers with AMD Ryzen first generation CPUs and computers with TPM 1.2 chips  despite the fact that Windows 11 can run well on these "incompatible" systems. Refrescar bypasses the CPU and TPM check during Windows 11 installation by safely modifying the Windows Registry.

**Refrescar works on computers running Windows 10 that are blocked from updating due to incompatible CPUs and TPM 1.2 only. Refrescar does not work on computers that are blocked from updating because they lack UEFI boot or because the contain no TPM module. Use [Microsoft's PC Health Check](https://aka.ms/GetPCHealthCheckApp) to see why your PC is blocked from updating.**
## Usage
TODO
 
## Contributing
1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin <project_name>/<location>`
5. Create the pull request.

Alternatively see the GitHub documentation on [creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).
