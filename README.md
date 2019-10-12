# unzip-with-correct-encoding

## Usage

    $ python3 unzip.py "file1.zip" "file2.zip"

You have to specify the original encoding and target encoding in unzip.py first.

## Why

The encoding of the file name is not recorded in zip files because the zip format standard did not require so, as a result when you try to extract files sent to you by others, the file name often becomes garbled. On macOS, many decompression software automatically guess the encoding. On Linux there are a lot of ways to specify the encoding manually, so it's not too much trouble. But on Windows, the system's own decompression software seems to have no place to set the encoding, there is no relevant settings in 7zip as well, and I don't like other paid software and adware either.

Recently I tried out the Windows operating system because I needed to use SolidWorks and several other Windows-only software.
Before, I have only used Windows in VMs, so unzipping files is not a problem, I can share the extracted folders to the VM.
However, when I try to use Windows standalone, I found that there is no GUI software like Keka or The Unarchiver that is easy to use under Windows, and I have not found any useful command line client. The only one that is more satisfying is 7zip. But it is buggy too.

This script was modified from [this dude's script](https://gist.github.com/hideaki-t/c42a16189dd5f88a955d), I added a bit of output to make it easier for me to know the progress and error messages.

以下机翻：

在 zip 格式压缩文件中，文件名的编码并没有被记录，因为 zip 格式标准没有如此要求。所以当你试图解压别人传给你的文件时，文件名经常会变成乱码。在 macOS 上，很多解压软件会自动推测其编码，所以一般问题不大。在 Linux 上一般都有办法手动指定编码，所以也不算麻烦。但是在 Windows 上，系统自带的解压似乎并没有什么地方可以设置编码，7zip里也没有相关的设置，我也不喜欢其他的收费软件和广告软件。

我最近尝试用了 Windows 操作系统，因为需要使用 SolidWorks 之类仅限 Windows 的软件。
在之前，我只在虚拟机里用过 Windows，所以解压不是问题，我可以把解压的文件夹分享给虚拟机。
然而，现在我尝试单独使用 Windows 的时候发现，在 Windows 下并没有类似 Keka 或者 The Unarchiver 那样容易使用的 GUI 软件，也没发现什么好用的命令行客户端。唯一一个比较让人满意的就是7zip。但它也有很多bug。

这个脚本是用[这位老兄的脚本](https://gist.github.com/hideaki-t/c42a16189dd5f88a955d)修改而来，稍微添加了一些输出，方便我知道进度和错误消息。
