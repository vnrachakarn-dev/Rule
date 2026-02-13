import os
import discord
from discord.ext import commands

# ====== ใส่ TOKEN จาก Environment ======
TOKEN = os.getenv("TOKEN")

# ====== ตั้งค่า BOT ======
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

# ====== EMBED DISCORD RULES ======
def discord_rules_embed():
    embed = discord.Embed(
        title="💤 Rules | กฎในดิสคอร์ด",
        description="""
🌐 **กฎทั่วไป**
🤝 ให้ความเคารพและให้เกียรติผู้อื่นเสมอ  
🗣️ พูดคำหยาบได้ แต่ต้องพอประมาณ  
🚫 ห้ามยาเสพติด ความรุนแรง อนาจาร  
📛 ห้ามสแปม  
😡 ห้ามดูหมิ่น เสียดสี  
🚫 ห้ามเหยียดเพศ ศาสนา ปมด้อย  
🎤 ประชุมห้ามพูดแทรก  
🎶 เพิ่มบอทเพลงต้องขออนุญาต  
👥 เชิญคนเข้าได้ แต่ต้องรับผิดชอบ  
📢 มีปัญหาแจ้ง Staff  
🏢 ห้ามทำลายภาพลักษณ์ MANAGER+  

💬 **ห้องระบาย**
😤 ใช้ ||สปอย|| หากมีคำหยาบ  

🔐 **ความปลอดภัย**
🛑 ห้ามแบล็คเมล์  
📣 โปรโมทห้าม 18+ / พนัน / โรล  

📌 **หมายเหตุ**
ทีมงานเปลี่ยนกฎได้โดยไม่แจ้งล่วงหน้า
""",
        color=0x2f3136
    )

    embed.set_image(url="https://media.giphy.com/media/7OH9z8lL8cnmkOxb6A/giphy.gif")
    embed.set_footer(text="Astra•Lis Community Rules")
    return embed


# ====== EMBED RP RULES ======
def rp_rules_embed():
    embed = discord.Embed(
        title="🎭 Roleplay Rules",
        description="""
🎭 IC → บทบาทในเกม  
👤 OC → ตัวตนจริง  
⚔️ DM → ฆ่าโดยไม่มีสตอรี่  
💪 PG → เก่งเกินมนุษย์  
🧠 MG → เอาความรู้ OOC มาใช้ IC  
👑 GM → ตัวละครเทพเกิน  
🔁 RK → ตายแล้วลืม 20 นาที  
💥 BK → ทำลายบรรยากาศ RP  
🏃 QG → ออกหนีบท  
💀 CK → ฆ่าตัวละครหนีสตอรี่  
❤️ VoL → ให้ค่าชีวิตเหมือนชีวิตจริง  
""",
        color=0xff0055
    )

    embed.set_image(url="https://media.giphy.com/media/7OH9z8lL8cnmkOxb6A/giphy.gif")
    embed.set_footer(text="The Lumina Roleplay System")
    return embed


# ====== BUTTON VIEW ======
class RulesView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="💤 กฎดิสคอร์ด", style=discord.ButtonStyle.gray)
    async def discord_rules(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.edit_message(embed=discord_rules_embed(), view=self)

    @discord.ui.button(label="🎭 กฎ Roleplay", style=discord.ButtonStyle.red)
    async def rp_rules(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.edit_message(embed=rp_rules_embed(), view=self)


# ====== COMMAND ======
@bot.command()
async def rules(ctx):
    await ctx.send(embed=discord_rules_embed(), view=RulesView())


# ====== BOT READY ======
@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")


# ====== RUN ======
bot.run(TOKEN)
