---
title: "如何批量重命名文件？3种方法详细教程"
date: 2024-01-20T00:00:00+08:00
draft: false
tags: ["教程", "批量重命名", "效率", "Windows"]
categories: ["实用技巧"]
description: "详细讲解Windows系统下批量重命名文件的3种方法：系统自带、PowerShell脚本、第三方工具"
---

## 快速答案

如果你赶时间，直接看结论：

| 方法 | 难度 | 适用场景 | 推荐度 |
|------|------|---------|--------|
| **系统自带** | 简单 | 简单序号命名 | ⭐⭐⭐ |
| **PowerShell** | 中等 | 复杂规则命名 | ⭐⭐⭐⭐⭐ |
| **第三方工具** | 简单 | 高级功能需求 | ⭐⭐⭐⭐⭐ |

---

## 方法一：Windows系统自带（最简单）

### 操作步骤

1. 选中要重命名的文件（按 `Ctrl+A` 全选，或 `Ctrl+点击` 多选）
2. 按 `F2` 或右键选择"重命名"
3. 输入新文件名，如 `照片`
4. 按 `Enter`

### 效果

系统会自动命名为：
- 照片 (1).jpg
- 照片 (2).jpg
- 照片 (3).jpg

### 优点
- 无需安装软件
- 操作简单

### 缺点
- 只能添加序号
- 无法自定义格式
- 无法批量替换文字

---

## 方法二：PowerShell脚本（最强大）

### 1. 批量添加前缀

```powershell
# 打开PowerShell，进入目标文件夹
cd D:\照片

# 给所有jpg文件添加前缀"旅行_"
Get-ChildItem *.jpg | Rename-Item -NewName { "旅行_" + $_.Name }
```

### 2. 批量替换文字

```powershell
# 将所有文件名的"旧文字"替换为"新文字"
Get-ChildItem | Rename-Item -NewName { $_.Name -replace "旧文字","新文字" }
```

### 3. 按序号重命名（自定义格式）

```powershell
# 按001, 002, 003格式重命名
$i = 1
Get-ChildItem *.jpg | ForEach-Object {
    $newName = "照片_{0:D3}.jpg" -f $i
    Rename-Item $_.Name -NewName $newName
    $i++
}
```

### 4. 添加日期前缀

```powershell
# 添加当前日期前缀
$date = Get-Date -Format "yyyyMMdd"
Get-ChildItem *.jpg | Rename-Item -NewName { $date + "_" + $_.Name }
```

### 5. 删除文件名中的特定文字

```powershell
# 删除所有文件名中的"副本"两个字
Get-ChildItem | Rename-Item -NewName { $_.Name -replace "副本","" }
```

### 优点
- 功能极其强大
- 可自定义任何规则
- 免费内置

### 缺点
- 需要学习命令
- 操作不当可能误改

---

## 方法三：第三方工具（最方便）

### 推荐工具：PowerRename（PowerToys）

**下载：** https://github.com/microsoft/PowerToys

**功能：**
- 正则表达式替换
- 预览修改结果
- 批量添加/删除文字
- 修改扩展名

**使用步骤：**
1. 安装PowerToys
2. 选中文件，右键选择"PowerRename"
3. 设置搜索和替换规则
4. 预览并应用

---

### 推荐工具：Advanced Renamer

**官网：** https://www.advancedrenamer.com

**功能：**
- 图形化界面
- 多种重命名方法
- 实时预览
- 支持元数据

**使用步骤：**
1. 添加文件
2. 选择重命名方法
3. 设置规则
4. 预览并执行

---

## 常见问题 FAQ

### Q: 重命名后文件打不开了怎么办？
A: 不要修改文件扩展名（如.jpg、.docx）。如果误改，改回原来的扩展名即可。

### Q: 可以撤销重命名吗？
A: 系统自带方法无法撤销。建议重命名前先备份，或使用支持撤销的第三方工具。

### Q: PowerShell命令执行报错怎么办？
A: 检查文件是否被占用，或路径是否正确。建议先在小批量文件上测试。

### Q: 如何按文件创建日期重命名？
A: 使用PowerShell：
```powershell
Get-ChildItem | Rename-Item -NewName { $_.CreationTime.ToString("yyyyMMdd") + "_" + $_.Name }
```

---

## 总结

- 简单需求 → **系统自带**
- 复杂规则 → **PowerShell**
- 图形化操作 → **PowerRename 或 Advanced Renamer**

掌握批量重命名技巧，处理几百个文件只需几秒钟！
