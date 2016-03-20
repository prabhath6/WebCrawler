import mechanize


def post_data():

    # url
    url_add = "http://www.indeed.com"

    # details
    details = {"q": "Python Developer", "l": "Santa Clara, CA"}

    # search based on job title and place
    browser = mechanize.Browser(factory=mechanize.RobustFactory())
    browser.set_handle_robots(False)

    # open the absloute url
    browser.open(url_add)

    # select the form
    browser.select_form(nr = 0)

    # fill the form
    browser.form["q"] = details.get("q", "")
    browser.form["l"] = details.get("l", "")

    return browser.submit()

if __name__ == "__main__":
    #import sys
    #sys.stdout.write(post_data().read())
    pass
