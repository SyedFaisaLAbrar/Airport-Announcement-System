import pandas as pd
from pydub import AudioSegment
from gtts import gTTS


def texttospeach(text, filename):
    ann_text = str(text)
    language = 'en'
    file = gTTS(text=ann_text, lang=language, slow=True)
    file.save(filename)


def mergeaudios(audiolist):
    combined = AudioSegment.empty()
    for audio in audiolist:
        combined += AudioSegment.from_mp3(audio)

    return combined


def generate_announcement():
    data = pd.read_excel("announce_English.xlsx")
    print(data)

    for index, item in data.iterrows():
        texttospeach(item['flight_no'] + " " + item['flight_name'], "2_english.mp3")
        texttospeach(item['from'], "4_english.mp3")
        texttospeach(item['to'], "6_english.mp3")
        texttospeach(item['platform'], "8_english.mp3")
        audios = [f"{i}_english.mp3" for i in range(1, 9)]
        processed_Audio = mergeaudios(audios)
        processed_Audio.export(f"Announcement for flight {item['flight_no']}.mp3", format="mp3")


def generate_template():
    text_1 = "Kindly attention for announcement. The flight number "
    texttospeach(text_1, "1_english.mp3")

    text_3 = " is takingoff from "
    texttospeach(text_3, "3_english.mp3")

    text_5 = "to "
    texttospeach(text_5, "5_english.mp3")

    text_7 = "at platform number "
    texttospeach(text_7, "7_english.mp3")


if __name__ == '__main__':
    print("Generating Template..........")
    generate_template()
    print("Generating Announcement..........")
    generate_announcement()
