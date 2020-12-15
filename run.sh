
for d in ../data/GO_PRO/test/*/sharp/*; do
  if [ -d "$d" ]; then
    echo $d
    dir="$d/*.png"
    for img in $dir; do
        echo $img
        python saliency_map.py --image $img
    done
  fi
done