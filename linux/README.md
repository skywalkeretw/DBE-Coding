# Linux
This is a quick guide to linux commands and tool that can be very usefull

if you want to try out the commands in a dev env please make sure docker is installed and use the following container as a test environment

The following command will put you into a ubuntu machine where you can try out the commands
```bash
docker run -it lukeroy/dbe-learn-linux:latest
```

---

## View file content
```bash
cat <filename>
```
examle inside the Test Environoment 
```bash
cat info.txt
```

## Create a new file
```bash
touch <file name>
```

## Delete a  file
```bash
rm <file name>
```

## Create a new directory
```bash
mkdir <dir name>
```

## Delete a  directory
```bash
rmmkdir <dir name>
```

## Delete a directory containing files
```bash
rm -rf <dir name>
```

---

## View Current Path
```bash
pwd
```

## Navigate into a folder
```bash
cd <dir name>
```

## Navigate out of the current folder
```bash
cd ..
```

## View current Directory content
```bash
ls
```
View it in list form
```bash
ls -la
```

---

## Create a ssh key this is used for logging onto a server or connecting to Github
```bash 
ssh-keygen
```
generate a ssh key called `ssh-key` without a password inside your `.ssh` directory 
```bash
ssh-keygen -f ~/.ssh/ssh-key -N ""
```

View your public key with cat the contend has to be copied to Github or the server you want to connect to
```bash
cat ~/.ssh/ssh-key.pub
```

## Connect to server over ssh
```bash
ssh <user>@<server>
```
live real example
```bash
ssh root@192.168.178.42
```

## Editing Files
To edit files you can use the teriminal editors Nano or Vim

Edit File using VIM
```bash
vim <file>
```
Exit vim: pres `esc` then type `wq` and press enter

```bash
nano <file>
```

