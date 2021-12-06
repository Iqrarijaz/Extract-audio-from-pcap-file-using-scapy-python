import pyshark
class Audio_Scraper:


    def scraper(self):
        rtp_list =[]
        pcap_file = ('audio.pcap')
        out_file = ("file.raw")
        print("Scraping: " + pcap_file)
        cap = pyshark.FileCapture(pcap_file,display_filter='rtp')
        raw_audio = open(out_file,'wb')

        for i in cap:
            try:
                rtp = i[3]
                if rtp.payload:
                    print(rtp.payload)
                    rtp_list.append(rtp.payload.split(":"))
            except:
                pass
        for rtp_packet in rtp_list:
            packet = " ".join(rtp_packet)
            print(packet)
            audio = bytearray.fromhex(packet)
            raw_audio.write(audio)
        print("\nFinished outputting raw audio: %s" % out_file)

        import wave

        with open(out_file, "rb") as inp_f:
            data = inp_f.read()
            with wave.open(out_file, "wb") as out_f:
                out_f.setnchannels(1)
                out_f.setsampwidth(2)  # number of bytes
                out_f.setframerate(44100)
                out_f.writeframesraw(data)


# pcap_test = Audio_Scraper("file.pcap","rtp","my_audio.raw").scraper()
