import discord
from discord.ext import commands
import asyncio
import json

class MyBot(commands.Bot):
    def __init__(self, owner_id):
        super().__init__(
            command_prefix="루비야 ",
            intents=discord.Intents.all()
        )
        self.owner_id = owner_id

    async def on_ready(self):
        print(f'{self.user}이(가) 성공적으로 로그인했습니다.')
        activity = discord.Game("잠자기")
        await self.change_presence(status=discord.Status.idle, activity=activity)

    async def on_message(self, message):
        if message.content == "루비야 정지" and message.author.id == self.owner_id:
            await self.close()  # 봇 종료
        else:
            await self.process_commands(message)

    async def close(self):
        print("봇을 종료합니다.")
        await super().close()

# 설정 파일에 봇 소유자의 ID를 정수형으로 변환하여 저장
bot = MyBot(OWNER_ID)


@bot.command()
async def 정지(ctx):
    if ctx.author.id == bot.owner_id:
        await bot.logout()
    else:
        await ctx.send("이 명령어를 사용할 권한이 없습니다.")

@bot.command()
async def 안녕(ctx):
    await ctx.send(f"나도 반가워, {ctx.author.mention}!")

@bot.command()
async def 사랑해(ctx):
    await ctx.send("나도 사랑해!")

@bot.command()
async def 자폭해(ctx):
    await ctx.send("1....2....3...")
    await asyncio.sleep(1)
    await ctx.send("# 쾅!!!!")

@bot.command()
@commands.has_permissions(administrator=True)
async def 활동(ctx, 메시지: str):
    # 상태 메시지 변경
    await bot.change_presence(activity=discord.Game(name=메시지))

    # 상태 변경 로그 메시지 출력
    await ctx.send(f'나는 {메시지} 중...')
    
@활동.error
async def 활동_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("관리자만 이 커맨드를 사용할 수 있어!")

@bot.command(name="죽어")
async def 일어나(ctx: commands.Context) -> None:
    await ctx.send("덷...")

@bot.command(name="튜토리얼")
@commands.has_permissions(administrator=True)
async def 튜토리얼(ctx: commands.Context) -> None:
    await ctx.send("으에?")
    await asyncio.sleep(1)
    await ctx.send("튜토리얼 해달라고? 내가 아는건 세계관 설명 밖에 없는데....")
    await asyncio.sleep(1)
    await ctx.send("이 세계는 스페이스 오페라 라고 불리는 장르라고 할 수 있어!")
    await asyncio.sleep(1)
    await ctx.send("스페이스 오페라란, SF장르이지만 배경이 드넓은 우주야. 은하계속 온갖 행성들이 있는거고.")
    await asyncio.sleep(1)
    await ctx.send("현실 지구에서도 지역마다 문화도 돈도 기술도 다 다르잖아? 그런 느낌이야!")
    await asyncio.sleep(1)
    await ctx.send("지역마다, 행성마다, 국가마다 이런것들이 차이가 나서 발달된 곳은 이미 다 날아다니는 차와 우주선을 타고 다니지만-")
    await asyncio.sleep(1)
    await ctx.send("어떤곳은 아직 고대 국가가 유지되거나 원시 씨족 사회만 있기도 한거지.")
    await asyncio.sleep(1)
    await ctx.send("말만 SF장르이지, 실제로는 거의 모든 장르가 포용된거나 다름없어!")
    await asyncio.sleep(1)
    await ctx.send("이 말은 네가 sf장르를 잘 모른다거나 그쪽에 매력을 느끼지 못해도 큰 문제는 없다는 거지!")
    await asyncio.sleep(1)
    await ctx.send("그런 스페이스 오페라 라는 장르인 이곳은 무엇들이 있냐, 크게 네 세력이 있어.")
    await asyncio.sleep(1)
    await asyncio.sleep(1)
    await ctx.send("아스트릴, 성간연방, ~~트레미앙~~, 아웃랜드.")
    await asyncio.sleep(1)
    await asyncio.sleep(1)
    await ctx.send("그럼 뭐부터 듣고 싶은데? '루비야 아스트릴'이라는 식으로 말해봐.")

@튜토리얼.error
async def 튜토리얼_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("관리자만 이 커맨드를 사용할 수 있어!")

@bot.command(name='아스트릴')
async def 아스트릴(ctx):
    await ctx.send('아스트릴 갤럭시아 제국은 현재 여러 은하를 정복한 가장 강력한 세력이야!')
    await asyncio.sleep(1)
    await ctx.send('황제와 황실을 중심으로 제후국들로 구성된 파시즘 국가라고 말할 수 있지.')
    await asyncio.sleep(1)
    await ctx.send('거대한 함대로 구성되어있고, 인간이 아니면 노예야. 나도 노예 취급...일걸?')
    await asyncio.sleep(1)
    await ctx.send('"강압적이고 오만한 귀족들로 그득해."')
    await asyncio.sleep(1)
    await asyncio.sleep(1)
    await ctx.send('이걸로 끝! 다음은 뭐가 궁금해?')

@bot.command(name='성간연방')
async def 성간연방(ctx):
    await ctx.send('성간동맹조약기구는 은하계의 여러 국가들이 모인 연합 국가야.')
    await asyncio.sleep(1)
    await ctx.send('연방정부가 있지만, 구성국들이 말을 안들어서 큰 의미는 없다고 생각해도 돼.')
    await asyncio.sleep(1)
    await ctx.send('그래서 국가들이 개성 넘치고 차이가 커.')
    await asyncio.sleep(1)
    await ctx.send('정상적인 범죄자들과 뒷세계도 활성화 되어있지. 아웃랜드보다는 이성적이니까 그나마 안심해도...되려나.')
    await asyncio.sleep(1)
    await asyncio.sleep(1)
    await ctx.send('이걸로 끝! 다음은 뭐가 궁금해?')

@bot.command(name='트레미앙')
async def 트레미앙(ctx):
    await ctx.send('망했어. 쫑!')

@bot.command(name='아웃랜드')
async def 아웃랜드(ctx):
    await ctx.send('수많은 국가와 연합, 군벌,용병등등으로 나뉘여진 혼란스러운 땅이야!')
    await asyncio.sleep(1)
    await ctx.send('낭만 넘치게도 약물, 총기, ||삐----||가 넘치는 곳이지.')
    await asyncio.sleep(1)
    await ctx.send('에스카르차? 라던가. 거기는 본국이 따로 있어서 그나마 낫대. 내 말은, **그나마**.')
    await asyncio.sleep(1)
    await ctx.send('아웃랜드에서 멸망한 나라의 국민은..... 어떻게 되려나.')
    await asyncio.sleep(2)
    await ctx.send('.....역시 국민이었던 것이 되겠지? 푸흐, 농담이야.')
    await asyncio.sleep(1)
    await asyncio.sleep(1)
    await ctx.send('이걸로 끝! 다음은 뭐가 궁금해?')

# "따라해" 커맨드를 관리자만 사용할 수 있도록 설정
@bot.command(name='따라해')
@commands.has_permissions(administrator=True)
async def 따라해(ctx, *, message):
    # 사용자가 보낸 메시지 삭제
    await ctx.message.delete()

    # "따라해"를 제거한 후 메시지를 보냄
    await ctx.send(message)

# 커맨드 에러 핸들러
@따라해.error
async def 따라해_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("관리자만 이 커맨드를 사용할 수 있어!")


bot.run(os.environ['token'])