import os

posts_dir = "D:\\my-blog\\content\\posts"

articles = [
    {
        "filename": "best-free-vpn-services.md",
        "title": "2026年最好用的免费VPN推荐：安全上网必备工具",
        "date": "2026-02-03",
        "tags": '["VPN", "隐私", "安全", "免费"]',
        "description": "2026年最可靠的免费VPN服务对比评测，保护隐私安全上网"
    },
    {
        "filename": "best-free-office-suites.md",
        "title": "2026年最好用的免费办公软件：替代Microsoft Office",
        "date": "2026-02-04",
        "tags": '["办公软件", "Office", "免费", "替代"]',
        "description": "2026年最强大的免费办公软件对比，包括LibreOffice、WPS、OnlyOffice等"
    },
    {
        "filename": "best-free-media-players.md",
        "title": "2026年最好用的免费视频播放器推荐",
        "date": "2026-02-05",
        "tags": '["播放器", "视频", "免费", "软件"]',
        "description": "2026年最实用的免费视频播放器对比评测，支持所有格式"
    },
    {
        "filename": "best-free-file-compression.md",
        "title": "2026年最好用的免费压缩软件：替代WinRAR",
        "date": "2026-02-06",
        "tags": '["压缩软件", "解压", "免费", "工具"]',
        "description": "2026年最可靠的免费压缩软件推荐，支持RAR、ZIP、7Z等格式"
    },
    {
        "filename": "best-free-download-managers.md",
        "title": "2026年最好用的免费下载工具：提升下载速度",
        "date": "2026-02-07",
        "tags": '["下载工具", "下载器", "免费", "效率"]',
        "description": "2026年最强大的免费下载管理器推荐，支持多线程和断点续传"
    },
    {
        "filename": "best-free-disk-cleanup-tools.md",
        "title": "2026年最好用的免费磁盘清理工具：释放存储空间",
        "date": "2026-02-08",
        "tags": '["磁盘清理", "存储", "免费", "优化"]',
        "description": "2026年最实用的免费磁盘清理软件，找出并删除大文件和垃圾文件"
    },
    {
        "filename": "best-free-backup-software.md",
        "title": "2026年最好用的免费备份软件：数据安全必备",
        "date": "2026-02-09",
        "tags": '["备份", "数据安全", "免费", "工具"]',
        "description": "2026年最可靠的免费备份软件推荐，自动备份重要文件和系统"
    },
    {
        "filename": "best-free-pdf-readers.md",
        "title": "2026年最好用的免费PDF阅读器：替代Adobe Reader",
        "date": "2026-02-10",
        "tags": '["PDF", "阅读器", "免费", "替代"]',
        "description": "2026年最轻量快速的免费PDF阅读器对比评测"
    },
    {
        "filename": "best-free-system-info-tools.md",
        "title": "2026年最好用的免费系统信息工具：查看硬件配置",
        "date": "2026-02-11",
        "tags": '["系统信息", "硬件", "免费", "工具"]',
        "description": "2026年最详细的免费系统信息检测工具推荐"
    },
    {
        "filename": "best-free-remote-desktop-tools.md",
        "title": "2026年最好用的免费远程桌面软件：远程办公必备",
        "date": "2026-02-12",
        "tags": '["远程桌面", "远程办公", "免费", "工具"]',
        "description": "2026年最流畅的免费远程桌面软件对比，支持跨平台远程控制"
    }
]

for article in articles:
    filepath = os.path.join(posts_dir, article["filename"])
    
    content = f"""---
title: "{article['title']}"
date: {article['date']}T00:00:00+08:00
draft: false
tags: {article['tags']}
categories: ["工具推荐"]
description: "{article['description']}"
---

## 快速答案

**最佳推荐：**
- 待补充

## 详细评测

### 1. 软件A

**优点：**
- 功能强大
- 完全免费

**缺点：**
- 学习曲线较陡

## 总结

2026年免费工具已经足够强大，根据需求选择即可。
"""
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Created: {article['filename']}")

print("Done! Created 10 articles.")
