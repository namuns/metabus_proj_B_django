
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import lost_pet_board.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LostPetBoard',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('lost_board_no', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(db_index=True, max_length=50)),
                ('status', models.CharField(choices=[('찾는중', '찾는중'), ('찾았어요', '찾았어요')], db_index=True, default='찾는중', max_length=20)),
                ('content', models.TextField()),
                ('pet_name', models.CharField(max_length=20)),
                ('animal_type', models.CharField(choices=[('개', '개'), ('고양이', '고양이')], default='개', max_length=10)),
                ('dog_breed', models.CharField(choices=[('전체', '전체'), ('기타', '기타'), ('믹스견', '믹스견'), ('모르겠어요', '모르겠어요'), ('골든리트리버', '골든리트리버'), ('래브라도 리트리버', '래브라도 리트리버'), ('그레이 하운드', '그레이 하운드'), ('그레이트 피레니즈', '그레이트 피레니즈'), ('아프간 하운드', '아프간 하운드'), ('닥스훈트', '닥스훈트'), ('달마시안', '달마시안'), ('도베르만', '도베르만'), ('로트와일러', '로트와일러'), ('셰퍼드', '셰퍼드'), ('말라뮤트', '말라뮤트'), ('말티즈', '말티즈'), ('푸들', '푸들'), ('스피츠', '스피츠'), ('볼 테리어', '볼 테리어'), ('보스턴 테리어', '보스턴 테리어'), ('슈나우져', '슈나우져'), ('보더콜리', '보더콜리'), ('불독', '불독'), ('비글', '비글'), ('비숑 프리제', '비숑 프리제'), ('빠삐용', '빠삐용'), ('사모예드', '사모예드'), ('삽살개', '삽살개'), ('샤페이', '샤페이'), ('시베리안 허스키', '시베리안 허스키'), ('시츄', '시츄'), ('시바', '시바'), ('코카 스파니엘', '코카 스파니엘'), ('오브차카', '오브차카'), ('요크셔테리어', '요크셔테리어'), ('치와와', '치와와'), ('차우차우', '차우차우'), ('웰시코기', '웰시코기'), ('페키니즈', '페키니즈'), ('진도개', '진도개'), ('포메라니안', '포메라니안'), ('퍼그', '퍼그')], default='전체', max_length=30)),
                ('cat_breed', models.CharField(choices=[('전체', '전체'), ('기타', '기타'), ('믹스묘', '믹스묘'), ('모르겠어요', '모르겠어요'), ('샴', '샴'), ('러시안 블루', '러시안 블루'), ('먼치킨', '먼치킨'), ('발레니즈', '발레니즈'), ('터키쉬 앙고라', '터키쉬 앙고라'), ('노르웨이 숲', '노르웨이 숲'), ('메인쿤', '메인쿤'), ('버만', '버만'), ('벵갈', '벵갈'), ('스핑크스', '스핑크스'), ('스코티쉬 폴드', '스코티쉬 폴드'), ('시베리안', '시베리안'), ('페르시안', '페르시안'), ('코리안 숏헤어', '코리안 숏헤어'), ('아메리칸 숏헤어', '아메리칸 숏헤어'), ('히말라얀', '히말라얀'), ('한국 고양이', '한국 고양이')], default='전체', max_length=30)),
                ('sex', models.CharField(choices=[('미상', '미상'), ('암컷', '암컷'), ('수컷', '수컷')], default='미상', max_length=10)),
                ('animal_tag', models.CharField(max_length=30)),
                ('lost_location', models.CharField(max_length=50)),
                ('lost_time', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-lost_board_no'],
            },
        ),
        migrations.CreateModel(
            name='LostPetBoardImage',
            fields=[
                ('lost_image_no', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='', validators=[lost_pet_board.models.validate_image])),
                ('lost_board_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='board_image', to='lost_pet_board.lostpetboard')),
            ],
            options={
                'ordering': ['-lost_image_no'],
            },
        ),
        migrations.CreateModel(
            name='LostPetBoardComment',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('lost_comment_no', models.AutoField(primary_key=True, serialize=False)),
                ('comment_content', models.TextField()),
                ('lost_board_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='lost_pet_board.lostpetboard')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['lost_comment_no'],
            },
        ),
    ]
