from mechanize import urljoin, urlopen, ParseResponse


def post_data(url_add, **kwargs):

    # search based on job title and place
    query = "jobs?q=&l="

    # open the absloute url
    response = urlopen(urljoin(url, query))

    # select the form
    forms = ParseResponse(response, backwards_compat=False)
    form = forms[0]

    # fill the form
    form["q"] = kwargs.get("q")
    form["l"] = kwargs.get("l")

    return urlopen(form.click()).read()

if __name__ == "__main__":

    # url to post the data.
    url = "http://www.indeed.com"
    post_data(url, q="Python Developer", l="Santa Clara, CA")

