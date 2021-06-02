import base64


def form(plain_text, attachments):
    mime = ''
    mime += 'MIME-Version: 1.0\n' \
         'Content-Type:multipart/mixed;boundary="KkK170891tpbkKk__FV_KKKkkkjjwq"\n'
    for attachment in attachments:
        mime += '\n--KkK170891tpbkKk__FV_KKKkkkjjwq\n'
        with open(f'date/{attachment}', 'rb') as f:
            content = f.read()
        encoded = base64.standard_b64encode(content).decode('ascii')
        filename = attachment.split('/')[-1]
        mime += f'Content-Type:application/octet-stream;name="{filename}"\n' \
                'Content-Transfer-Encoding:base64\n' \
                f'Content-Disposition:attachment;filename="{filename}"\n' \
                '\n\r' \
                f'{encoded}'
    mime += '\n--KkK170891tpbkKk__FV_KKKkkkjjwq\n'
    mime += 'Content-Type: text/plain; charset=utf-8\n' \
                      '\n\r' \
                      f'{plain_text}'
    mime += '\n--KkK170891tpbkKk__FV_KKKkkkjjwq--\n'
    return mime