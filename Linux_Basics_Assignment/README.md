# Linux Commands Assignment

## 1. Creating and Renaming Files/Directories
```bash
mkdir test_dir
cd test_dir
touch example.txt
mv example.txt renamed_example.txt
```
## 2. Viewing File Contents
```bash
cat /etc/passwd
head -n 5 /etc/passwd
tail -n 5 /etc/passwd
```
## 3. Searching for Patterns 
```bash
cat /etc/passwd | grep "root" -n
```
## 4. Zipping and Unzipping
```bash
cd assignments
zip -r test_dir.zip test_dir
unzip test_dir.zip -d unzipped_dir
```
## 5. Making a Request &  Downloading Files
```bash
curl https://jsonplaceholder.typicode.com/todos/1
wget https://jsonplaceholder.typicode.com/todos/1
```
## 6. Changing Permissions
```bash
touch secure.txt
ls -a -l
chmod 444 secure.txt
ls -a -l
```
## 7. Working with Environment Variables
```bash
export MY_VAR="Hello, Linux"
echo $MY_VAR

