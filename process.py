
from sys import argv

f1 = open(arv[1], "r").read()
f2 = open(arv[1], "r").read()

frame_data = {}

class results:
  mac80211_hwsim_tx_frame_nl = 0
  hwsim_tx_info_frame_received_nl = 0
  hwsim_cloned_frame_received_nl = 0
  process_messages_cb = 0
  send_tx_info_frame_nl = 0
  send_cloned_frame_msg = 0

def make_device_key(d, k):
  if not d in frame_data:
    frame_data[d] = {}
  if not k in frame_data[d]:
    frame_data[d][k] = results

def populate_data(f):
  for line in f.split("\n"):
    tokens = line.split("\t");
    if "mac80211_hwsim_tx_frame_nl" in tokens:
        make_device_key(tokens[tokens.index("mac80211_hwsim_tx_frame_nl")+1], tokens[tokens.index("mac80211_hwsim_tx_frame_nl")+2])
        frame_data[tokens.index("mac80211_hwsim_tx_frame_nl")+1][tokens.index("mac80211_hwsim_tx_frame_nl")+2].mac80211_hwsim_tx_frame_nl = int(tokens[tokens.index("mac80211_hwsim_tx_frame_nl")+3])
    elif "hwsim_tx_info_frame_received_nl" in tokens:
        make_device_key(tokens[tokens.index("hwsim_tx_info_frame_received_nl")+1], tokens[tokens.index("hwsim_tx_info_frame_received_nl")+2])
        frame_data[tokens.index("hwsim_tx_info_frame_received_nl")+1][tokens.index("hwsim_tx_info_frame_received_nl")+2].mac80211_hwsim_tx_frame_nl = int(tokens[tokens.index("hwsim_tx_info_frame_received_nl")+3])
    elif "hwsim_cloned_frame_received_nl" in  tokens:
        make_device_key(tokens[tokens.index("hwsim_cloned_frame_received_nl")+1], tokens[tokens.index("hwsim_cloned_frame_received_nl")+2])
        frame_data[tokens.index("hwsim_cloned_frame_received_nl")+1][tokens.index("hwsim_cloned_frame_received_nl")+2].mac80211_hwsim_tx_frame_nl = int(tokens[tokens.index("hwsim_cloned_frame_received_nl")+3])
    elif "process_messages_cb" in tokens:
        make_device_key(tokens[tokens.index("process_messages_cb")+1], tokens[tokens.index("process_messages_cb")+2])
        frame_data[tokens.index("process_messages_cb")+1][tokens.index("process_messages_cb")+2].mac80211_hwsim_tx_frame_nl = int(tokens[tokens.index("process_messages_cb")+3])
    elif "send_tx_info_frame_nl" in tokens:
        make_device_key(tokens[tokens.index("send_tx_info_frame_nl")+1], tokens[tokens.index("send_tx_info_frame_nl")+2])
        frame_data[tokens.index("send_tx_info_frame_nl")+1][tokens.index("send_tx_info_frame_nl")+2].mac80211_hwsim_tx_frame_nl = int(tokens[tokens.index("send_tx_info_frame_nl")+3])
    elif "send_cloned_frame_msg" in tokens:
        make_device_key(tokens[tokens.index("send_cloned_frame_msg")+1], tokens[tokens.index("send_cloned_frame_msg")+2])
        frame_data[tokens.index("send_cloned_frame_msg")+1][tokens.index("send_cloned_frame_msg")+2].mac80211_hwsim_tx_frame_nl = int(tokens[tokens.index("send_cloned_frame_msg")+3])

def print_data():
    for hw in frame_data:
        print hw
        for f in frame_data[hw]:
            print "Frame %d" % int(f)
            if frame_data[hw][f].mac80211_hwsim_tx_frame_nl != 0 and frame_data[hw][f].process_messages_cb != 0:
                print "\td->w: %d" % (frame_data[hw][f].process_messages_cb - frame_data[hw][f].mac80211_hwsim_tx_frame_nl)
            if frame_data[hw][f].hwsim_tx_info_frame_received_nl != 0 and frame_data[hw][f].send_tx_info_frame_nl != 0:
                print "\tw_i->d_i: %d" % (frame_data[hw][f].hwsim_tx_info_frame_received_nl - frame_data[hw][f].send_tx_info_frame_nl)
            if frame_data[hw][f].hwsim_cloned_frame_received_nl != 0 and frame_data[hw][f].send_cloned_frame_msg != 0:
                print "\tw_f->d_f: %d" % (frame_data[hw][f].hwsim_cloned_frame_received_nl - frame_data[hw][f].send_cloned_frame_msg)
            if frame_data[hw][f].send_cloned_frame_msg != 0 and frame_data[hw][f].process_messages_cb != 0:
                print "\tt_src->t_dst: %d" % (frame_data[hw][f].send_cloned_frame_msg - frame_data[hw][f].process_messages_cb)
            if frame_data[hw][f].mac80211_hwsim_tx_frame_nl != 0 and frame_data[hw][f].hwsim_cloned_frame_received_nl != 0:
                print "\tr_src->r_dst: %d" % (frame_data[hw][f].hwsim_cloned_frame_received_nl - frame_data[hw][f].mac80211_hwsim_tx_frame_nl)

populate_data()
print_data()
