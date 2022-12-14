import os
import torch


# python preprocess_sign.py data/ori/test.txt data/processed/test.pt

# python preprocess.py --source-lang pt --target-lang pt --testpref data/processed/test --destdir data-bin/ --dataset-impl raw





folder = "./i3d-features-gustavo/span=16_stride=2/"
test_signer = "gabriel"

#open("./data/ori/train.txt", "w").close()
open("./data/ori/test.txt", "w").close()
open("test.sign-pt.sign", "w").close()
#open("train.sign-pt.sign", "w").close()

with open('./New_Libraria_Texts.txt', 'r', encoding="utf8") as f:
    lines = f.readlines()
    f.close()

i = 0

for pt in os.listdir(folder):

    for line in lines:

        video = line.split(";")[0]
        frase = line.split(";")[-1].lower()

        if video in pt:

            i += 1

            print(i, pt)

            filename = pt.split(".")[0]

            array = torch.load(folder+pt)

            json = "{\"ident\": "+ "\""+filename+"\", "+"\"size\": "+str(len(array))+"}, "

            with open('./data/ori/test.txt', 'a', encoding="utf8") as f:
                f.write(frase)
                f.close()
            with open('./test.sign-pt.sign', 'a', encoding="utf8") as f:
                f.write(json)
                f.close()

            """
            if not test_signer in filename:
                with open('./data/ori/train.txt', 'a', encoding="utf8") as f:
                    f.write(frase)
                    f.close()
                with open('./train.sign-pt.sign', 'a', encoding="utf8") as f:
                    f.write(json)
                    f.close()
            else:
                with open('./data/ori/test.txt', 'a', encoding="utf8") as f:
                    f.write(frase)
                    f.close()
                with open('./test.sign-pt.sign', 'a', encoding="utf8") as f:
                    f.write(json)
                    f.close()
            """
            break