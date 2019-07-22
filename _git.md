1. 在本地使用git clone方法获取
    `git clone https://github.com/szmzaid1904/WebChat.git`
2. 创建本地分支
   `git branch 名称_dev`
3. 将本地分支推送给远程仓库
   `git push -u origin  名称_dev`

### 获取某远程分支的某份文件替换当前分支的当前文件
`git checkout branch -- filename`  
如： 分支test上有一个文件A，你在test1分支上， 此时如果想用test分支上的A文件替换test1分支上的文件的话，可以使用git checkout test1, 然后git checkout test -- A

### 记得时时同步master和远程master一致