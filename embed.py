from dhooks import Embed

class Embed:

    embed = Embed(title="Embed Title", color=0xFFFFFF, timestamp='now')  # Change FFFFFF with your color in hex form

    embed.set_author(name="Author", icon_url="https://i.imgur.com/AD3MbBi.jpeg")  # Change url with your direct image link

    embed.add_field(name="Field Name", value="This is a test field")

    embed.set_thumbnail(
            url="https://c.tenor.com/dFBNnUW7TbIAAAAd/sad-cats.gif")  # Change url with your direct image link

    embed.set_footer(text="Footer Field")
