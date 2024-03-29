# 全键盘操作 vscode

参考：https//blog.csdn.net/geerniya/article/details/79830914

## mac 按键表

- `⌘` == `cmd`
- `⇧` == `shift`
- `⇪` == `Caps Lock`
- `⌥` == `Option`
- `⌃` == `Control`
- `↩` == `Return/enter`
- `⌫` == `Delete`
- `⌦` == `向前删除键（Fn+Delete）`
- `↑` == `上箭头`
- `↓` == `下箭头`
- `←` == `左箭头`
- `→` == `右箭头`
- `⇞` == `Page Up（Fn+↑）`
- `⇟` == `Page Down（Fn+↓）`
- `Home` == `Fn + ←`
- `end` == `Fn + →`
- `⇥` == `右制表符（Tab键）`
- `⇤` == `左制表符（shift+Tab）`
- `⎋` == `escape (esc)`
- `⏏` == `电源开关键`

## 快捷键

### 通用

- `ctrl + a\e` 移动到行首、行末
- `cmd + left\right` 移动到行首、行末
- `ctrl + p\n` 上、下
- `ctrl + f\b` 左、右
- `option + left/right` 左、右（按单词）
- `ctrl + k\backspace` 删除到行末、行尾
- `ctrl + h\d` 向左、右删除
- `ctrl + pgUp\pgDown` 滚动屏幕

### 基本编辑

- `fn + left/right` 跳转到行首/行末
- `fn + down/up` 光标移动到下一页/上一页
- `fn + cmd + down/up` 屏幕滚动到下一页/上一页
- `cmd + shift + \` 光标跳转到匹配的括号
- `cmd + up/down` 光标移动到文件首/文件尾
- `cmd + left/right` 光标移动到行首/行尾
- `alt + up` 向上移动一行
- `alt + down` 向下移动一行
- `option + cmd + ] / [` 展开、折叠
- `option + left/right` 光标按单词移动
- `ctrl + option + left/right` 光标按单词大小写分解移动光标
- `option + shift + a` 添加、移除块注释
- `cmd + k + u` 改为大写
- `cmd + k + l` 改为小写
- `ctrl + -`后退
- `cmd + k + k` 删除光标右侧内容
- `cmd + delete` 删除光标右侧内容

### 查找替换

- `cmd + g` 查找下一个
- `cmd + shift + g` 查找上一个
- `shift + cmd + \` 跳转到括号
- `ctrl + cmd + shift + right/left` 扩大选择和缩小选择块
- `cmd + e` 选中全部
- `cmd + f` 查找
- `cmd + option + f` 替换
- `cmd + d` 向下选中相同内容
- `cmd + k cmd + d` 移除前一个向下选中相同内容
- **`option + enter` 选中所有匹配项**
- **`cmd + shift + space` 向上选中**
- \*\* `cmd + t` 在工作区中查找符号
- \*\* `cmd + shift + o` 在当前文件查找符号

### 视图

- **`ctrl + q` 切换视图**
- `cmd + down` 在侧边栏打开文件
- `cmd + 0`/ `cmd+shift+e` 到侧边栏
- `cmd + ctrl + left` 将当前文件在新编辑器打开
- `ctrl + \` 切出一个新的编辑器（最多 3 个
- **`ctrl + cmd + left/right` 将文件切换到新的编辑器**
- `cmd + B` 显示、隐藏侧边栏
- `cmd + shift + ]/[` 切换编辑窗口
- `cmd + shift + e` 显示资源管理器 或 切换焦点
- `cmd + shift + f` 显示搜索框
- `ctrl + shift + g` 显示 Git 面板
- `cmd + shift + d` 显示调试面板
- `cmd + shift + x` 显示插件面板
- `cmd + shift + h` 全局搜索替换
- `cmd + shift + j` 显示、隐藏高级搜索
- `cmd + shift + c` 打开新终端
- `cmd + shift + u` 显示输出面板
- `cmd + j` 切换面板
- `cmd + shift + v` Markdown 预览窗口
- `cmd + k v` 分屏显示` Markdown 预览窗口
- `cmd + k cmd + s` 打开快捷键

### 进价

- **`cmd + k m` 更改文件语言**
- `option + shift + f` 格式化
- `cmd + k cmd + f` 格式化选中内容
- **`cmd + k cmd + x` 删除行尾多余空格**
- `ctrl + shift + up/down` 光标向上或者向下多行选取
- `option + 点击` 插入多光标
- `option + cmd + r` 用正则表达式查找
- `ctrl + j` 合并行
- **`ctrl + cmd + left` 将当前页新开编辑窗口打开**

### 组合键

### 文件管理

`cmd + k cmd + w` 全部关闭
`cmd + k r` 在资源管理器中查看当前文件

## 关键配置

```json
{
    "terminal.integrated.fontFamily" "Source Code Pro for Powerline",
    "workbench.editor.enablePreviewFromQuickOpen" false
    "vetur.format.options.tabSize": 4,
    "vetur.format.defaultFormatter.js": "vscode-typescript",// 工作目录用，自己项目可以用默认
    "vetur.format.defaultFormatterOptions": {
      "prettier": {
          "singleQuote": true,
          "eslintIntegration": true
      }
    },
	"javascript.format.insertSpaceBeforeFunctionParenthesis": true
}
```

## 快捷键配置

```bash
// Place your key bindings in this file to overwrite the defaults
[
  {
    "key" "cmd+]",
    "cmd" "workbench.action.nextSideBarView",
    "when" "sideBarFocus"
  },
  {
    "key" "cmd+[",
    "cmd" "workbench.action.previousSideBarView",
    "when" "sideBarFocus"
  },
  {
    "key" "cmd+]",
    "cmd" "workbench.action.nextPanelView",
    "when" "panelFocus"
  },
  {
    "key" "cmd+[",
    "cmd" "workbench.action.previousPanelView",
    "when" "panelFocus"
  }
]
```

## 插件

- bookmark
- coderunner
- Color Highlight
- editorConfig for vs code
- eslint
- Git History
- Git Lens
- Markdown Preview Github Styling
- markdownlint
- npm
- Open HTML in Default Browser
- Partial Diff
- Project Manager
- Settings Sync
- Sublime Text Keymap and Settings Importer
- Vetur
- Vue VSCode Snippets
- vscode-icons
- File Utils
- Quokka.js 实时运行 js 的 demo
- Bracket Pair Colorizer 2 高亮括号内容
- REST Client 配合 chrome 获取请求，在编辑器中显示
