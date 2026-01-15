#!/usr/bin/env python3
"""
簡單的系統資訊顯示腳本
"""
import platform
import datetime

def main():
    print("=== 系統資訊 ===")
    print(f"作業系統: {platform.system()}")
    print(f"版本: {platform.release()}")
    print(f"Python 版本: {platform.python_version()}")
    print(f"目前時間: {datetime.datetime.now()}")

if __name__ == "__main__":
    main()
