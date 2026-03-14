import base64
p = r'C:\Users\uiade\AppData\Roaming\Claude\local-agent-mode-sessions\6d42a371-6c20-4798-96c4-63b9b2662cbb\5eef6b87-08aa-4ba0-817c-4dc20a6d84eb\local_a0e66508-87de-435a-8e3b-44e7747b45ca\uploads\TruCycle_Pitch_Deck_SEIS_v4.pptx'
out = r'C:\Users\uiade\AppData\Roaming\Claude\local-agent-mode-sessions\6d42a371-6c20-4798-96c4-63b9b2662cbb\5eef6b87-08aa-4ba0-817c-4dc20a6d84eb\local_a0e66508-87de-435a-8e3b-44e7747b45ca\uploads\pptx_b64.txt'
d = open(p, 'rb').read()
print('SIZE:' + str(len(d)))
with open(out, 'w') as f:
    f.write(base64.b64encode(d).decode())
print('DONE')
