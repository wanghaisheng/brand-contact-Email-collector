domain="${URL}"

# Use the input variable value in your script
echo "The value of 'myInput' is: $domain"
python emailall.py --domain $domain run > result/$domain.txt
