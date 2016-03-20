import post_using_mechanize


def get_data():
    fd = post_using_mechanize.post_data().read()
    fs = fd.split('"')
    data = 0

    for i in fs:
        if "jobmap[" in i and " = " in i:
            data = i.split(" = ")
            break

    each_post = []
    data_dict = {}

    for i in data[1].split("\n"):
        if len(i) > 20:
            post = i.split("= ")
            each_post.append(post[1])

    for e_post in each_post:
        for j in e_post.split(","):
            f = j.split(":")
            if len(f) == 2:
                data_dict[str(f[0])] = f[1]
        print_details(data_dict)


def print_details(data_dict):
    print "Company: {} \ntitle: {} \ncity: {} \ncountry: {}" \
        .format(data_dict['cmp'], data_dict['title'], data_dict["city"], data_dict["country"])
    print


if __name__ == "__main__":
    get_data()
