sudo adduser cloudlet --ingroup wheel \
&& sudo nmcli radio wifi on \
&& sudo nmcli device wifi connect cloudlet password my-secure-password \
&& sudo nmcli connection modify cloudlet connection.autoconnect-priority 100 \
&& sudo nmcli connection delete "ut-public"