domain="${URL}"

# Use the input variable value in your script
echo "The value of 'myInput' is: $domain"

if [ ! -d "result" ]; then
  mkdir result
fi

python emailall.py --domain $domain run   >> result/$domain.txt
