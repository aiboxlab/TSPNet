
import test_scripts.rouge_local as local
from test_scripts.bleu_local import compute_bleu


def filtrar(lines, frase):
	filtered = filter(lambda line: line.replace(" ","").replace("\n","") != frase.replace(" ","").replace("\n",""), lines)
	return list(filtered)

def compute_cvpr_bleu(hyps, refs, max_order=4):
	tokenized_hyps = []
	tokenized_refs = []
	for h in hyps:
		tokenized_hyps.append(h.split())
	for r in refs:
		tokenized_refs.append([r.split()])
	bleu_all_orders = []
	for i in list(range(1, max_order+1)):
		bleu, precisions, bp, ratio, translation_length, reference_length = compute_bleu(tokenized_refs, tokenized_hyps, max_order=i)
		bleu_all_orders.append(round(bleu * 100, 2))
	return bleu_all_orders

def compute_rouge_bleu(hyp, ref):
	r = local.rouge([hyp], [ref])['rouge_l/f_score']*100
	b = compute_cvpr_bleu([hyp], [ref])
	return r, b



"""
hyps = []
refs = []
rouges = []
bleus = []

with open("tspnet_nl_gisleile_usuarios.txt", encoding="utf-8") as f:
	lines = f.readlines()
	f.close()

for line in lines:

	if line == "\n":
		continue

	frase_pred = line.split(" || ")[0].replace("\n", "").lower()
	frase_gt = line.split(" || ")[1].replace("\n", "").lower()

	r, b = compute_rouge_bleu(frase_pred, frase_gt)

	hyps.append(frase_pred)
	refs.append(frase_gt)
	rouges.append(r)
	bleus.append(b)


zipped = zip(rouges, bleus, hyps, refs)
sorted_pairs = sorted(zipped, reverse=True)
tuples = zip(*sorted_pairs)
rouges, bleus, hyps, refs = [ list(tup) for tup in tuples ]

bleus1 = [bleu[0] for bleu in bleus]
bleus2 = [bleu[1] for bleu in bleus]
bleus3 = [bleu[2] for bleu in bleus]
bleus4 = [bleu[3] for bleu in bleus]

print(sum(rouges)/len(rouges))


for i in range(len(rouges)):
	#print(hyps[i], "===", refs[i])
	#print(hyps[i])
	#print(refs[i])
	#print('{0:.2f}'.format(rouges[i]))
	#print('{0:.2f}'.format(bleus[i][3]))
	#print('{0:.2f}'.format(bleus[i][0]), '{0:.2f}'.format(bleus[i][1]), '{0:.2f}'.format(bleus[i][2]), '{0:.2f}'.format(bleus[i][3]))
	#print()
"""









with open("New_Libraria_Texts.txt", encoding="utf-8") as f:
	lines = f.readlines()
	f.close()

with open("nl_usuariogisleile_GUSTAVO_16.BW_04.A_1.test.txt", encoding="utf-8") as f:
	preds = f.readlines()
	f.close()


videos = []
hyps = []
refs = []
rouges = []
bleus = []


i = 0
for line in lines:

	video_gt = line.split(";")[0]
	frase_gt = line.split(";")[-1].replace("\n", "").lower()

	for pred in preds:

		video_pred = pred.split(" || ")[0]
		frase_pred = pred.split(" || ")[1].replace("\n", "").lower()

		if video_gt in video_pred:

			i += 1
			#print(i)
			#print("GT:", frase_gt, "\nPRED:" , frase_pred)

			r, b = compute_rouge_bleu(frase_pred, frase_gt)

			#print(r, b, "\n")

			videos.append(video_pred)
			hyps.append(frase_pred)
			refs.append(frase_gt)
			rouges.append(r)
			bleus.append(b)


zipped = zip(rouges, bleus, hyps, refs, videos)
#sorted_pairs = sorted(zipped, reverse=True)
sorted_pairs = zipped
tuples = zip(*sorted_pairs)
rouges, bleus, hyps, refs, videos = [ list(tup) for tup in tuples ]

bleus1 = [bleu[0] for bleu in bleus]
bleus2 = [bleu[1] for bleu in bleus]
bleus3 = [bleu[2] for bleu in bleus]
bleus4 = [bleu[3] for bleu in bleus]

print(sum(rouges)/len(rouges))
print(sum(bleus1)/len(rouges))
print(sum(bleus2)/len(rouges))
print(sum(bleus3)/len(rouges))
print(sum(bleus4)/len(rouges))

"""
for i in range(len(rouges)):
	#print(videos[i])
	#print(hyps[i], "===", refs[i])
	#print(hyps[i])
	#print(refs[i])
	print('{0:.2f}'.format(rouges[i]), '{0:.2f}'.format(bleus[i][0]), '{0:.2f}'.format(bleus[i][1]), '{0:.2f}'.format(bleus[i][2]), '{0:.2f}'.format(bleus[i][3]))
	#print("ROUGE:",'{0:.2f}'.format(rouges[i]))
	#print('{0:.2f}'.format(bleus[i][3]))
	#print("BLEUS:",'{0:.2f}'.format(bleus[i][0]), '{0:.2f}'.format(bleus[i][1]), '{0:.2f}'.format(bleus[i][2]), '{0:.2f}'.format(bleus[i][3]))
	#print()
"""