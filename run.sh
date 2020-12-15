
for d in ../data/GO_PRO/test/*/sharp/*; do
  echo "$d"
  python saliency_map.py --image $d
done