import urllib.request

if __name__ == '__main__':
    link = "https://snaptron.cs.jhu.edu/gtex/snaptron?regions=CD99&sfilter=SMTS:Brain"

    # Open the URL and iterate over the lines
    with urllib.request.urlopen(link) as response:
        data = []
        header = []
        samples=set()
        for i, line in enumerate(response):
            # if i >345:
            #    break
            # Decode bytes to string (assuming UTF-8 encoding)
            decoded_line = line.decode('utf-8')
            decoded_line = decoded_line.strip()
            # header
            if decoded_line=="":
                continue
            if i == 0:
                header = decoded_line.split("\t")
            else:
                current_data=decoded_line.split("\t")
                samples.update(x.split(":")[0] for x in current_data[12].split(","))
                data.append(current_data)
        print(f"{len(header)}x{i}x{len(samples)}")
        for index,row in enumerate(zip(header, data[5])):
            attribute, value =row
            print(f"{index}:{attribute}->{value}")
