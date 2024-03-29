define N = Character('', color="#333333")
define U = Character('???', color="#333333")
define I = Character('ふわり', color="#333333")
define M = Character('ママ', color="#333333")

label start:

    stop music

    scene bg room_1
    with dissolve

    U "「たこ焼きが食べたいなぁ･･･。」"

    play music "1.mp3"

    U "私の名前は{rb}霞音{/rb}{rt}かすみね{/rt}ふわり。"

    I "私は今、無性にたこ焼きが食べたくなっている。"

    I "それもそのはず、今日のテレビで見たグルメ特集で紹介されていた、外はサクサク、中はトロトロのたこ焼きが頭から離れないからだ。"

    I "「あの番組で見たたこ焼き...外はこんがりと焼けてて、中は溶けるよう...すごく美味しそうだった！」"

    I "そういえば、家の近くにある商店街に、小さなたこ焼き屋さんがあったはず...もう待ってられない、今すぐ食べに行こう！"

    I "「ママ、今日の夜ご飯はいいから、外で食べてくるね！」"

    M "「いいわよ、でも遅くならないでね！」"

    I "「大丈夫だって、行ってくる！」"

    I "そう言って、私は急いで家を出た。"
    
    scene bg street_1
    with dissolve

    I "「この辺りだったはず...あ、見つけた！」"

    I "いつも学校帰りに良い匂いを漂わせている、道沿いの小さなたこ焼き屋さん「たこのすけ」。"

    I "通りすがりには何度も見ていたけれど、入るのはこれが初めて。どんな味がするのかな？ワクワクしながら店に足を踏み入れた。"

    scene bg shop
    with dissolve

    N "店内は小さくて居心地が良い雰囲気で、壁には色とりどりのたこ焼きの写真が飾られている。"

    N "店主は温かい笑顔で私を迎え、「いらっしゃい！何にする？」と尋ねた。"

    I "「あの、おすすめのたこ焼きはありますか？」"

    N "店主は嬉しそうに目を輝かせ、「もちろん！当店自慢の『特製チーズたこ焼き』をお勧めするよ。外はカリカリ、中はとろ～りチーズが溶けているんだ」と答える。"

    I "「それにします！あと、甘いソースとピリ辛マヨネーズも付けてください！」"

    N "店主は「了解！」と応じて、たこ焼きを焼き始める。ふわりは店内を見渡し、他の客たちが楽しそうに食事をしている様子を眺める。"

    N "ふわりは、たこ焼きが焼けるのを待ちながら、店内の温かい雰囲気に浸っていた。"

    stop music

    N "しばらくすると、店主が「はい、お待たせ！特製チーズたこ焼きだよ」と言って、熱々のたこ焼きを出してくれる。"

    scene bg takoyaki
    with dissolve

    play music "2.mp3"

    I "「わぁ、美味しそう！」"

    N "ふわりは早速、たこ焼きを一つ口に運ぶ。熱さと美味しさに、思わず「あつっ！でも、すごく美味しい！」と声をあげる。"

    I "「このたこ焼き、外側はこんがりとしていてカリカリの食感があるけど、中はとろっとろ。たこ焼きの中にあるタコの味がしっかりしていて、この食感がたまらないわ...」"

    I "「それに、この特製のソースとマヨネーズがたこ焼きの味を引き立ててる。ソースはちょうど良い甘みとコクがあり、ピリ辛のマヨネーズがアクセントになっている。まるでたこ焼きのために、特別に作られたような絶妙な味わいだ！」"

    I "「中のチーズがとろける感じも最高！口の中でチーズがとろけて、たこ焼きと一緒に広がるクリーミーさが、もう...言葉にできないくらい美味しいーーー！」"

    N "その瞬間、店内の他の客たちはふわりの反応に笑いながら、彼女に親しげに話しかけ始める。"

    N "そうして、ふわりはたこ焼きを食べながら、地元の人たちとの交流を楽しむのだった..."

    scene bg street_2
    with dissolve

    I "「あー、美味しかった！」"
    
    N "終わり"

    return
