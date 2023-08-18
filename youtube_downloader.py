from pytube import YouTube

while True:
    print("""
            İŞLEM SEÇİNİZ
        1 - Video İndirme
        2 - Sadece Video Sesini İndirme
        0 - Çıkış
        """)

    selected = int(input("Yapmak istediğiniz işlemi seçiniz : "))

    if selected == 1:

        url = input("Video Linki : ")
        out_path = ""
        yt = YouTube(url).streams.get_highest_resolution().download(out_path)

        print(f"""
            Video Konumu : {yt.title()}
            Video Süresi : {yt.__len__()}

            Bulunduğunuz klasörü kontrol ediniz!
            """)
        

    elif selected == 2:
        url = input("Video Linki : ")
        out_path = ""
        yt = YouTube(url).streams.get_audio_only().download(out_path)
        
        print(f"""
            Video Konumu : {yt.title()}
            Video Süresi : {yt.__len__()}

            Bulunduğunuz klasörü kontrol ediniz!
            """)
        

    
    elif selected == 0:
        break
    
    else:
        print("Lütfen geçerli bir işlem seçiniz!")
