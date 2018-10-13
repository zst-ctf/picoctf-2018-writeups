for value in {1..65600}; do
	echo "Collecting $value"
    nc 2018shell2.picoctf.com 3609 | sed 's/:/ =/g' >> out.txt
    echo >> out.txt
done


