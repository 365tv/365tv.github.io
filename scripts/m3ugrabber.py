#! /usr/bin/python3
banner = r'''
#EXTINF:-1 tvg-name="VTV1 HD - Thời sự tổng hợp" tvg-id="vtv1hd" tvg-logo="https://assets-vtvcab.gviet.vn/images/logos/VTV1_HD_M.png" group-title="Kênh VTV" catchup="append" catchup-days="0.3" catchup-source="https://tshift.fptplay.net/dvr/vtv1hd_1000.stream/chunks_dvr_range-${start}-10800.m3u8",VTV1 HD
https://livecdn.fptplay.net/hda1/vtv1hd_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 tvg-name="VTV2 HD - Khoa học & giáo dục" tvg-id="vtv2hd" tvg-logo="https://assets-vtvcab.gviet.vn/images/logos/VTV2_HD_M.png" group-title="Kênh VTV" catchup="append" catchup-days="0.3" catchup-source="https://tshift.fptplay.net/dvr/vtv2_2000.stream/chunks_dvr_range-${start}-10800.m3u8",VTV2 HD
https://livecdn.fptplay.net/hda1/vtv2_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 tvg-name="VTV3 HD - Thể thao - giải trí và thông tin kinh tế" tvg-id="vtv3hd" tvg-logo="https://assets-vtvcab.gviet.vn/images/logos/VTV3_HD_M.png" group-title="Kênh VTV" catchup="append" catchup-days="0.3" catchup-source="https://tshift.fptplay.net/dvr/vtv3hd_1500.stream/chunks_dvr_range-${start}-10800.m3u8",VTV3 HD
https://livecdn.fptplay.net/hda1/vtv3hd_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 tvg-name="VTV4 HD - Truyền hình Việt Nam ở nước ngoài" tvg-id="vtv4hd" tvg-logo="https://assets-vtvcab.gviet.vn/images/logos/VTV4_HD_M.png" group-title="Kênh VTV" catchup="append" catchup-days="0.3" catchup-source="https://tshift.fptplay.net/dvr/vtv4_2000.stream/chunks_dvr_range-${start}-10800.m3u8",VTV4 HD
https://livecdn.fptplay.net/hda1/vtv4_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 tvg-name="VTV5 HD - Truyền hình dân tộc" tvg-id="vtv5hd" tvg-logo="https://assets-vtvcab.gviet.vn/images/logos/VTV5_HD_M.png" group-title="Kênh VTV" catchup="append" catchup-days="0.3" catchup-source="https://tshift.fptplay.net/dvr/vtv5hd_1500.stream/chunks_dvr_range-${start}-10800.m3u8",VTV5 HD
https://livecdn.fptplay.net/hda2/vtv5hd_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 tvg-name="VTV5 TNB HD - Truyền hình Việt Nam khu vực Tây Nam Bộ" tvg-id="vtv5hdtnb" tvg-logo="https://vtvgo-image.vtvdigital.vn/images/7__.png" group-title="Kênh VTV",VTV5 Tây Nam Bộ
https://mutixx5hq1liv.akamaized.net/vtv5tnb/vtv5tnb@720p.m3u8
#EXTINF:-1 tvg-name="VTV5 TN HD - Truyền hình Việt Nam khu vực Tây Nguyên" tvg-id="vtv5hdtn" tvg-logo="https://vtvgo-image.vtvdigital.vn/images/163__.png" group-title="Kênh VTV",VTV5 Tây Nguyên
https://mutixx5hq1liv.akamaized.net/vtv5tn/vtv5tn@720p.m3u8
#EXTINF:-1 tvg-name="VTV6 HD - Truyền hình thanh thiếu niên" tvg-id="vtv6hd" tvg-logo="https://assets-vtvcab.gviet.vn/images/logos/VTV6_HD_M.png" group-title="Kênh VTV" catchup="append" catchup-days="0.3" catchup-source="https://tshift.fptplay.net/dvr/vtv6hd_1500.stream/chunks_dvr_range-${start}-10800.m3u8",VTV6 HD
https://livecdn.fptplay.net/hda1/vtv6hd_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 tvg-name="VTV7 HD - Truyền hình giáo dục" tvg-id="vtv7hd" tvg-logo="https://assets-vtvcab.gviet.vn/images/logos/VTV7_HD_M.png" group-title="Kênh VTV" catchup="append" catchup-days="0.3" catchup-source="https://tshift.fptplay.net/dvr/vtv7hd_1500.stream/chunks_dvr_range-${start}-10800.m3u8",VTV7 HD
https://livecdn.fptplay.net/hda3/vtv7hd_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 tvg-name="VTV8 HD - Truyền hình quốc gia khu vực miền Trung Tây Nguyên" tvg-id="vtv8hd" tvg-logo="https://assets-vtvcab.gviet.vn/images/logos/VTV8_HD_M.png" group-title="Kênh VTV" catchup="append" catchup-days="0.3" catchup-source="https://tshift.fptplay.net/dvr/vtv8hd_1500.stream/chunks_dvr_range-${start}-10800.m3u8",VTV8 HD
https://livecdn.fptplay.net/hda2/vtv8hd_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 tvg-name="VTV9 HD - Truyền hình quốc gia khu vực miền Nam" tvg-id="vtv9hd" tvg-logo="https://assets-vtvcab.gviet.vn/images/logos/VTV9_HD_M.png" group-title="Kênh VTV" catchup="append" catchup-days="0.3" catchup-source="https://tshift.fptplay.net/dvr/vtv9_1500.stream/chunks_dvr_range-${start}-10800.m3u8",VTV9 HD
https://livecdn.fptplay.net/hda2/vtv9_vhls.smil/chunklist_b5000000.m3u8

#EXTINF:-1 tvg-name="VTVCab 1 - Vie GIẢITRÍ" tvg-id="vtvcab1hd" tvg-logo="https://imgstatic.vtvcab.vn/logos/GIAITRI_TV_HD_M.png" group-title="Kênh VTVCab" type="stream",VTVCab1 - Vie GIẢITRÍ SD
https://e3.endpoint.cdn.sctvonline.vn/hls/vtvcab1/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 tvg-name="VTVCab 1 - Vie GIẢITRÍ" tvg-id="vtvcab1hd" tvg-logo="https://imgstatic.vtvcab.vn/logos/GIAITRI_TV_HD_M.png" group-title="Kênh VTVCab" type="stream",VTVCab1 - Vie GIẢITRÍ HD
http://gg.gg/VieGIAITRIHD
#EXTINF:-1 tvg-name="VTVCab 2 - Kênh Phim truyện Việt Nam" tvg-id="vtvcab2hd" tvg-logo="https://mytv.com.vn/upload/channel/phpMg6DY5_613966915655d.png" group-title="Kênh VTVCab" type="stream",VTVCab2 - ON Phim Việt
https://e3.endpoint.cdn.sctvonline.vn/hls/vtvcab2/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 tvg-name="VTVCab 3 - Kênh thể thao" tvg-id="vtvcab3hd" tvg-logo="https://mytv.com.vn/upload/channel/phpLhy8IQ_613966bf6fda5.png" group-title="Kênh VTVCab" type="stream",VTVCab3 - On Sports
https://e3.endpoint.cdn.sctvonline.vn/hls/vtvcab3/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 tvg-name="VTVCab 4 HD - Kênh phim truyện và giải trí đa phương tiện" tvg-id="vtvcab4hd" tvg-logo="https://lienket.vn/VTVCab4" group-title="Kênh VTVCab" type="stream",VTVCab4 - LOVE TV
https://e3.endpoint.cdn.sctvonline.vn/hls/vtvcab4/sd2/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 tvg-name="VTVCab 5 - Kênh phim truyện và giải trí tổng hợp" tvg-id="vtvcab5hd" tvg-logo="https://imgstatic.vtvcab.vn/logos/E_CHANNEL_M.png" group-title="Kênh VTVCab" type="stream",VTVCab5 - E-CHANNEL
https://e3.endpoint.cdn.sctvonline.vn/hls/vtvcab5/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 tvg-name="VTVCab 6 - Kênh thể thao giải trí và thông tin kinh tế" tvg-id="vtvcab6hd" tvg-logo="https://mytv.com.vn/upload/channel/phpI5Z2Qu_60d191d31bb2a.png" group-title="Kênh VTVCab" type="stream",VTVCab6 - ON Sports +
https://e3.endpoint.cdn.sctvonline.vn/hls/vtvcab6/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 tvg-name="VTVCab 7 - Kênh Sức khỏe và Cuộc sống" tvg-id="vtvcab7hd" tvg-logo="https://mytv.com.vn/upload/channel/phprtQ6hB_5dae811aae9cd.png" group-title="Kênh VTVCab" type="stream",VTVCab7 - Sức khỏe và Cuộc sống
https://e3.endpoint.cdn.sctvonline.vn/hls/vtvcab7/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 tvg-name="VTVCab 8 - Kênh thiếu nhi BiBi" tvg-id="vtvcab8hd" tvg-logo="https://mytv.com.vn/upload/channel/102.png" group-title="Kênh VTVCab" type="stream",VTVCab8 - BIBI
https://e3.endpoint.cdn.sctvonline.vn/hls/vtvcab8/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 tvg-name="VTVCab 9 - Kênh thiếu nhi BiBi" tvg-id="vtvcab9hd" tvg-logo="https://mytv.com.vn/upload/channel/195.png" group-title="Kênh VTVCab" type="stream",VTVCab9 - InfoTV
https://e3.endpoint.cdn.sctvonline.vn/hls/vtvcab9/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 tvg-name="VTVCab 10 - Kênh phim truyện" tvg-id="vtvcab10hd" tvg-logo="https://mytv.com.vn/upload/channel/phpHCeMwp_613966db69f11.png" group-title="Kênh VTVCab" type="stream",VTVCab10 - ON Cine
https://e3.endpoint.cdn.sctvonline.vn/hls/vtvcab10/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 tvg-name="VTVCab 11 - Kênh Mua sắm" tvg-id="" tvg-logo="https://shop-media.vgsshop.vn/pub/media/logo/stores/7/gsshop-logo.png" group-title="Kênh VTVCab" type="stream",VTVCab11 - GS SHOP (HTVC VGS SHOP Home Shopping)
https://e3.endpoint.cdn.sctvonline.vn/hls/vtvcab11/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 tvg-name="VTVCab 12 - Kênh thời trang, phong cách sống" tvg-id="vtvcab12hd" tvg-logo="https://mytv.com.vn/upload/channel/103.png" group-title="Kênh VTVCab" type="stream",VTVCab12 - Style TV
https://e3.endpoint.cdn.sctvonline.vn/hls/vtvcab12/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 tvg-name="VTVCab 13 - Kênh Mua sắm" tvg-id="" tvg-logo="https://vtvhyundai.vn/resource/img/logo_og.png" group-title="Kênh VTVCab" type="stream",VTVCab13 - VTV Hyundai Home Shopping
https://livecdn.fptplay.net/sdb/vtvhyundai_hls.smil/chunklist_b2500000.m3u8
#EXTINF:-1 tvg-name="VTVCab 15 - Kênh Âm nhạc" tvg-id="vtvcab15hd" tvg-logo="https://static.wikia.nocookie.net/logopedia/images/1/1e/VTVCab_15.png/revision/latest/scale-to-width-down/250?cb=20200206095612" group-title="Kênh VTVCab" type="stream",VTVCab15 - UM Channel
https://e3.endpoint.cdn.sctvonline.vn/hls/vtvcab15/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 tvg-name="VTVCab 16 HD - Kênh thể thao (điển hình về bóng đá)" tvg-id="vtvcab16hd" tvg-logo="https://mytv.com.vn/upload/channel/phpubyhmB_613966fbf1584.png" group-title="Kênh VTVCab" type="stream",VTVCab16 - ON Football SD
https://e3.endpoint.cdn.sctvonline.vn/hls/vtvcab16/sd2/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 tvg-name="VTVCab 17 - Kênh giải trí dành cho giới trẻ" tvg-id="vtvcab17hd" tvg-logo="https://mytv.com.vn/upload/channel/104.png" group-title="Kênh VTVCab" type="stream",VTVCab 17 - Yeah1TV
https://e3.endpoint.cdn.sctvonline.vn/hls/vtvcab17/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 tvg-name="VTVCab 19 - Vie DRAMAS" tvg-id="vtvcab19hd" tvg-logo="https://imgstatic.vtvcab.vn/logos/D_DRAMAS_HD_M.png" group-title="Kênh VTVCab" type="stream",VTVCab19 - Vie DRAMAS SD
https://e3.endpoint.cdn.sctvonline.vn/hls/vtvcab19/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 tvg-name="VTVCab 19 - Vie DRAMAS" tvg-id="vtvcab19hd" tvg-logo="https://imgstatic.vtvcab.vn/logos/D_DRAMAS_HD_M.png" group-title="Kênh VTVCab" type="stream",VTVCab19 - Vie DRAMAS HD
http://gg.gg/VieDRAMASHD
#EXTINF:-1 tvg-name="VTVCab 20 - Kênh giải trí dành cho phụ nữ và gia đình" tvg-id="vtvcab20hd" tvg-logo="https://mytv.com.vn/upload/channel/104.png" group-title="Kênh VTVCab" type="stream",VTVCab20 - VFamily
https://e3.endpoint.cdn.sctvonline.vn/hls//index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 tvg-name="SCTV1 HD - Kênh Hài" tvg-id="sctv1hd" tvg-logo="https://lienket.vn/SCTV1HD" group-title="Kênh SCTV" type="stream",SCTV1 HD - Hài
https://e1.endpoint.cdn.sctvonline.vn/hls/sctv1/sd2/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 tvg-name="SCTV2 HD - Kênh NetStars" tvg-id="sctv2hd" tvg-logo="https://lienket.vn/SCTV2" group-title="Kênh SCTV" type="stream",SCTV2 HD - NetStars
https://e1.endpoint.cdn.sctvonline.vn/hls/sctv2/sd2/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 tvg-name="SCTV3 HD - Kênh thiếu nhi" tvg-id="sctv3hd" tvg-logo="https://lienket.vn/SCTV3" group-title="Kênh SCTV" type="stream",SCTV3 HD - SEE TV
https://e1.endpoint.cdn.sctvonline.vn/hls/sctv3/sd2/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 tvg-name="SCTV3 HD - Kênh Giải Trí Tổng Hợp" tvg-id="sctv4hd" tvg-logo="https://lienket.vn/SCTV4" group-title="Kênh SCTV" type="stream",SCTV4 - Giải Trí Tổng Hợp
https://e1.endpoint.cdn.sctvonline.vn/hls/sctv4/sd2/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 tvg-name="SCTV5 - Kênh mua sắm" tvg-id="sctv5hd" tvg-logo="https://lienket.vn/SCTV5" group-title="Kênh SCTV" type="stream",SCTV5 - SCJ TV Shopping
https://e1.endpoint.cdn.sctvonline.vn/hls/sctv5/sd2/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 tvg-name="SCTV6 - Kênh Truyền hình giải trí thế hệ mới" tvg-id="sctv6hd" tvg-logo="https://lienket.vn/SCTV6" group-title="Kênh SCTV" type="stream",SCTV6 - FIM360
https://e1.endpoint.cdn.sctvonline.vn/hls/sctv6/sd2/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 tvg-name="SCTV6 HD - Kênh Phim FILM360 " tvg-id="sctv6hd" tvg-logo="http://img-zlr1.tv360.vn/image1/2021/07/01/13/1625121016367/0dc4f535839a_640_360.png" group-title="Kênh SCTV" type="stream",SCTV6 HD - FIM360 HD
https://livecdn.fptplay.net/hda3/film360_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 tvg-name="SCTV7 - Kênh Sân khấu văn nghệ tổng hợp" tvg-id="sctv7_hd" tvg-logo="https://lienket.vn/SCTV7" group-title="Kênh SCTV" type="stream",SCTV7 - SHOW TV
https://e1.endpoint.cdn.sctvonline.vn/hls/sctv7/sd2/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 tvg-name="SCTV8 - Kênh VITV Kinh Tế" tvg-id="sctv8hd" tvg-logo="https://lienket.vn/SCTV8" group-title="Kênh SCTV" type="stream",SCTV8 - VITV Kinh Tế
https://e1.endpoint.cdn.sctvonline.vn/hls/sctv8/sd2/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 tvg-name="SCTV9 HD - Kênh Phim Châu Á" tvg-id="sctv9hd" tvg-logo="https://lienket.vn/SCTV9" group-title="Kênh SCTV" type="stream",SCTV9 HD - Phim Châu Á & TVB
https://e1.endpoint.cdn.sctvonline.vn/hls/sctv9/sd2/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 tvg-name="SCTV10 - Kênh mua sắm thuộc Home Shopping Việt Nam" tvg-id="sctv10hd" tvg-logo="https://lienket.vn/SCTV10" group-title="Kênh SCTV" type="stream",SCTV10 - VTV Hyundai Home Shopping
https://e1.endpoint.cdn.sctvonline.vn/hls/sctv10/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 tvg-name="SCTV11 HD - Kênh Văn Hoá Nghệ Thuật" tvg-id="sctv11hd" tvg-logo="https://lienket.vn/SCTV11HD" group-title="Kênh SCTV" type="stream",SCTV11 HD - TV STAR
https://e1.endpoint.cdn.sctvonline.vn/hls/sctv11/sd2/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 tvg-name="SCTV12 HD -Kênh Du Lịch Khám Phá" tvg-id="sctv12hd" tvg-logo="https://lienket.vn/SCTV12" group-title="Kênh SCTV" type="stream",SCTV12 HD - Du Lịch & Khám Phá
https://e1.endpoint.cdn.sctvonline.vn/hls/sctv12/sd2/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 tvg-name="SCTV13 HD -Kênh Phụ nữ & Gia đình" tvg-id="sctv13hd" tvg-logo="https://lienket.vn/SCTV13" group-title="Kênh SCTV" type="stream",SCTV13 - Lady TV
https://e1.endpoint.cdn.sctvonline.vn/hls/sctv13/sd2/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 tvg-name="SCTV14 HD - Kênh Phim Việt" tvg-id="sctv14hd" tvg-logo="https://lienket.vn/SCTV14HD" group-title="Kênh SCTV" type="stream",SCTV 14 HD - Phim Việt
https://e1.endpoint.cdn.sctvonline.vn/hls/sctv14/sd2/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 tvg-name="SCTV15 HD - Kênh Ssport 2" tvg-id="sctv15hd" tvg-logo="https://lienket.vn/SCTV15" group-title="Kênh SCTV" type="stream",SCTV15 HD - Ssport 2
https://e1.endpoint.cdn.sctvonline.vn/hls/sctv15/sd2/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 tvg-name="SCTV16 HD - Kênh Phim Nước Ngoài Đặc Sắc" tvg-id="sctv16hd" tvg-logo="https://lienket.vn/SCTV16HD" group-title="Kênh SCTV" type="stream",SCTV16 HD - Phim Nước Ngoài Đặc Sắc
https://e1.endpoint.cdn.sctvonline.vn/hls/sctv16/sd2/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 tvg-name="SCTV17 HD - Kênh Thể Thao Ssport" tvg-id="sctv17hd" tvg-logo="https://lienket.vn/SCTV17HD" group-title="Kênh SCTV" type="stream",SCTV17 HD - Ssport
https://e1.endpoint.cdn.sctvonline.vn/hls/sctv17/sd2/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 tvg-name="SCTV18 - Kênh dành cho thanh thiếu niên" tvg-id="sctv18hd" tvg-logo="https://lienket.vn/SCTV18" group-title="Kênh SCTV" type="stream",SCTV18 - Kênh 18
https://e1.endpoint.cdn.sctvonline.vn/hls/sctv18/sd2/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 tvg-name="SCTV19 - Kênh dành cho teen" tvg-id="sctv19hd" tvg-logo="https://lienket.vn/SCTV19" group-title="Kênh SCTV" type="stream",SCTV19 - Channel T
https://e1.endpoint.cdn.sctvonline.vn/hls/sctv19/sd2/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 tvg-name="SCTV20 - Kênh nhạc bolero và nhạc trẻ" tvg-id="sctv20hd" tvg-logo="https://lienket.vn/SCTV20" group-title="Kênh SCTV" type="stream",SCTV20 - Ca nhạc tổng hợp
https://e1.endpoint.cdn.sctvonline.vn/hls/sctv20/sd2/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 tvg-name="SCTV Phim Tổng Hợp HD" tvg-id="sctvhdpth" tvg-logo="https://lienket.vn/SCTVPhimTH" group-title="Kênh SCTV" type="stream",SCTV Phim Tổng Hợp
https://e1.endpoint.cdn.sctvonline.vn/hls/sctvphimtonghop/sd2/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 tvg-name="SCTV21 HD - Kênh Việt Nam Ký Ức" tvg-id="sctv21hd" tvg-logo="https://chungplay.github.io/logo/SCTV21.png" group-title="Kênh SCTV" type="stream",SCTV21 HD - Việt Nam Ký Ức
https://e1.endpoint.cdn.sctvonline.vn/hls/sctv21/sd2/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 tvg-name="SCTV22 - Kênh SSport 1" tvg-id="sctv22hd" tvg-logo="https://lienket.vn/SCTV22" group-title="Kênh SCTV" type="stream",SCTV22 - Ssport 1
https://e1.endpoint.cdn.sctvonline.vn/hls/sctv22/sd2/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 tvg-name="BTV5 - Kênh SSport 3" tvg-id="btv5hd" tvg-logo="https://lienket.vn/BTV5" group-title="Kênh SCTV" type="stream",BTV5  - Ssport 3
https://e2.endpoint.cdn.sctvonline.vn/hls/btv5/sd2/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 tvg-id="vtc1hd" tvg-name="VTC1 HD" tvg-logo="https://mytv.com.vn/upload/channel/75.png" group-title="Kênh VTC | FPT Play" catchup="append" catchup-days="0.3" catchup-source="https://tshift.fptplay.net/dvr/vtc1_1500.stream/chunks_dvr_range-${start}-10800.m3u8",VTC1 HD
https://livecdn.fptplay.net/hda1/vtc1_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 tvg-id="vtc2" tvg-name="VTC2 HD" tvg-logo="https://mytv.com.vn/upload/channel/21.png" group-title="Kênh VTC | FPT Play" catchup="append" catchup-days="0.3" catchup-source="https://tshift.fptplay.net/dvr/vtc2_1000.stream/chunks_dvr_range-${start}-10800.m3u8", VTC2 HD
https://livecdn.fptplay.net/sdb/vtc2_hls.smil/chunklist_b2500000.m3u8
#EXTINF:-1 tvg-id="vtc3hd" tvg-name="VTC3 HD" tvg-logo="https://mytv.com.vn/upload/channel/83.png" group-title="Kênh VTC | FPT Play" catchup="append" catchup-days="0.3" catchup-source="https://tshift.fptplay.net/dvr/vtc3_1000.stream/chunks_dvr_range-${start}-10800.m3u8",VTC3 HD
https://livecdn.fptplay.net/hda1/vtc3hd_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 tvg-id="vtc4hd" tvg-name="VTC4 HD" tvg-logo="https://mytv.com.vn/upload/channel/134.png" group-title="Kênh VTC | FPT Play" catchup="append" catchup-days="0.3" catchup-source="https://tshift.fptplay.net/dvr/vtc4_1000.stream/chunks_dvr_range-${start}-10800.m3u8",VTC4 HD
https://livecdn.fptplay.net/hda2/vtc4_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 tvg-id="vtc5hd" tvg-name="VTC5 HD" tvg-logo="https://mytv.com.vn/upload/channel/187.png" group-title="Kênh VTC | FPT Play" catchup="append" catchup-days="0.3" catchup-source="https://tshift.fptplay.net/dvr/vtc5_1000.stream/chunks_dvr_range-${start}-10800.m3u8",VTC5 HD
https://livecdn.fptplay.net/sdb/vtc5_hls.smil/chunklist_b2500000.m3u8
#EXTINF:-1 tvg-id="vtc6hd" tvg-name="VTC6 HD" tvg-logo="https://mytv.com.vn/upload/channel/23.png" group-title="Kênh VTC | FPT Play" catchup="append" catchup-days="0.3" catchup-source="https://tshift.fptplay.net/dvr/vtc6_1000.stream/chunks_dvr_range-${start}-10800.m3u8", VTC6 HD
https://livecdn.fptplay.net/sdb/vtc6_hls.smil/chunklist_b2500000.m3u8
#EXTINF:-1 tvg-id="vtc7hd" tvg-name="VTC7 HD" tvg-logo="https://mytv.com.vn/upload/channel/188.png" group-title="Kênh VTC | FPT Play" catchup="append" catchup-days="0.3" catchup-source="https://tshift.fptplay.net/dvr/vtc7_1000.stream/chunks_dvr_range-${start}-10800.m3u8", VTC7 HD
https://livecdn.fptplay.net/sdb/todaytv_hls.smil/chunklist_b2500000.m3u8
#EXTINF:-1 tvg-id="vtc8" tvg-name="VTC8 HD" tvg-logo="https://mytv.com.vn/upload/channel/164.png" group-title="Kênh VTC | FPT Play" catchup="append" catchup-days="0.3" catchup-source="https://tshift.fptplay.net/dvr/vtc8_1000.stream/chunks_dvr_range-${start}-10800.m3u8",VTC8 HD
https://livecdn.fptplay.net/sdb/vtc8_hls.smil/chunklist_b2500000.m3u8
#EXTINF:-1 tvg-id="vtc9hd" tvg-name="VTC9 HD" tvg-logo="https://mytv.com.vn/upload/channel/189.png" group-title="Kênh VTC | FPT Play" catchup="append" catchup-days="0.3" catchup-source="https://tshift.fptplay.net/dvr/vtc9_1000.stream/chunks_dvr_range-${start}-10800.m3u8",VTC9 HD
https://livecdn.fptplay.net/sdb/vtc9_hls.smil/chunklist_b2500000.m3u8
#EXTINF:-1 tvg-id="vtc10hd" tvg-name="VTC10 HD" tvg-logo="https://mytv.com.vn/upload/channel/116.png" group-title="Kênh VTC | FPT Play" catchup="append" catchup-days="0.3" catchup-source="https://tshift.fptplay.net/dvr/vtc10_1000.stream/chunks_dvr_range-${start}-10800.m3u8", VTC10 HD
https://livecdn.fptplay.net/sdb/vtc10_hls.smil/chunklist_b2500000.m3u8
#EXTINF:-1 tvg-id="vtc11" tvg-name="VTC11 HD" tvg-logo="https://mytv.com.vn/upload/channel/26.png" group-title="Kênh VTC | FPT Play" catchup="append" catchup-days="0.3" catchup-source="https://tshift.fptplay.net/dvr/vtc11_1000.stream/chunks_dvr_range-${start}-10800.m3u8", VTC11 HD
https://livecdn.fptplay.net/sdb/vtc11_hls.smil/chunklist_b2500000.m3u8
#EXTINF:-1 tvg-id="vtc12" tvg-name="VTC12 HD" tvg-logo="https://mytv.com.vn/upload/channel/phpWgYcFl_5e1d3209b5e25.png" group-title="Kênh VTC | FPT Play" catchup="append" catchup-days="0.3" catchup-source="https://tshift.fptplay.net/dvr/vtc12_1000.stream/chunks_dvr_range-${start}-10800.m3u8", VTC12 HD
https://livecdn.fptplay.net/sdb/vtc12_hls.smil/chunklist_b2500000.m3u8
#EXTINF:-1 tvg-id="vtc13hd" tvg-name="VTC13 HD" tvg-logo="https://mytv.com.vn/upload/channel/78.png" group-title="Kênh VTC | FPT Play" catchup="append" catchup-days="0.3" catchup-source="https://tshift.fptplay.net/dvr/vtc13_1000.stream/chunks_dvr_range-${start}-10800.m3u8",VTC13 HD
https://livecdn.fptplay.net/hda1/vtc13_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 tvg-id="vtc14hd" tvg-name="VTC14 HD" tvg-logo="https://mytv.com.vn/upload/channel/207.png" group-title="Kênh VTC | FPT Play" catchup="append" catchup-days="0.3" catchup-source="https://tshift.fptplay.net/dvr/vtc14_1000.stream/chunks_dvr_range-${start}-10800.m3u8",VTC14 HD
https://livecdn.fptplay.net/hda1/vtc14_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 tvg-id="vtc16" tvg-name="VTC16 HD" tvg-logo="https://mytv.com.vn/upload/channel/206.png" group-title="Kênh VTC | FPT Play" catchup="append" catchup-days="0.3" catchup-source="https://tshift.fptplay.net/dvr/vtc16_1000.stream/chunks_dvr_range-${start}-10800.m3u8",VTC16 HD
https://livecdn.fptplay.net/sdb/vtc16_2000.stream/chunklist.m3u8

#EXTINF:-1 tvg-logo="http://imageidc1.tv360.vn/image1/2020_09_23/1600823412691/61627b84a612_640_360.png" group-title="Kênh Hanoicab"  type="stream",Hanoicab1 - HiTV
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://live2cdn.todayplus.com.vn/sdb/smil:hitv.smil/chunklist_b1596000.m3u8
#EXTINF:-1 tvg-logo="http://imageidc1.tv360.vn/image1/2020_09_23/1600823396313/7b474bf7bbce_640_360.png" group-title="Kênh Hanoicab"  type="stream",Hanoicab2 - YouTV
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://livecdn.fptplay.net/sdb/youtv_hls.smil/chunklist_b2500000.m3u8

#EXTINF:-1 tvg-id="musicbox" tvg-logo="https://fvmpqluto0obj.vcdn.cloud/Media/files/channels/thumb_1623738494c_Box%20Movie.png" group-title="Kênh INTHEBOX.TV" ,BOX Movie¹ HD
https://e4.endpoint.cdn.sctvonline.vn/hls/boxmovie1/sd2/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 tvg-id="hollywoodclassics" tvg-logo="https://fvmpqluto0obj.vcdn.cloud/Media/files/channels/thumb_1623742686c_Hollywood-201.png" group-title="Kênh INTHEBOX.TV" ,Hollywood Classics HD
https://e4.endpoint.cdn.sctvonline.vn/hls/hollywood/sd2/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 tvg-id="inthebox" tvg-logo="https://fvmpqluto0obj.vcdn.cloud/Media/files/channels/thumb_1623926685c_BOX%20W.png"  group-title="Kênh INTHEBOX.TV" , In The Box
http://103.195.238.226/inthebox/mpegts
#EXTINF:-1 tvg-id="boxhits" tvg-logo="https://fvmpqluto0obj.vcdn.cloud/Media/files/channels/thumb_1626834087channel3_BoxHit.png"  group-title="Kênh INTHEBOX.TV" , Box Hits
http://103.195.238.226/boxhits/mpegts
#EXTINF:-1 tvg-id="man" tvg-logo="http://img-zlr1.tv360.vn/image1/2021/08/02/18/1627902182400/125faee2618c_640_360.png"  group-title="Kênh INTHEBOX.TV" , MAN
http://103.195.238.226/man/mpegts
#EXTINF:-1 tvg-id="musicbox" tvg-logo="https://fvmpqluto0obj.vcdn.cloud/Media/files/channels/thumb_1623738727c_Music%20Box.png" group-title="Kênh INTHEBOX.TV" , Music Box
https://e4.endpoint.cdn.sctvonline.vn/hls/boxmusic/sd2/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 tvg-id="woman" tvg-logo="https://fvmpqluto0obj.vcdn.cloud/Media/files/channels/thumb_1623743214c_Woman-193.png" group-title="Kênh INTHEBOX.TV" ,Woman HD
https://e4.endpoint.cdn.sctvonline.vn/hls/woman/sd2/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1  tvg-id="planetearthhd" tvg-logo="http://img-zlr1.tv360.vn/image1/2020_09_23/1600823484363/34cadc4f9c06_640_360.png" group-title="Kênh INTHEBOX.TV" ,Planet Earth HD
https://e4.endpoint.cdn.sctvonline.vn/hls/planetearth/sd2/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 tvg-id="happykids" tvg-logo="http://img-zlr1.tv360.vn/image1/2020_09_23/1600823512270/ee08dd0e8b64_640_360.png" group-title="Kênh INTHEBOX.TV" ,Happy Kids HD
https://e4.endpoint.cdn.sctvonline.vn/hls/happykid/sd2/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 tvg-id="drfithd" tvg-logo="http://img-zlr1.tv360.vn/image1/2020_09_23/1600822429190/7b74ab00eb3e_640_360.png" group-title="Kênh INTHEBOX.TV" ,Dr.Fit HD
https://e4.endpoint.cdn.sctvonline.vn/hls/drfit/sd2/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 tvg-id="vtc1hd" group-title="Kênh VTC | VTC now" tvg-logo="https://s3.amazonaws.com/studiopro-app-vtc/assets/images/vtc1_thumbnail.jpg" type="stream",VTC1 HD
https://vtc130121.cdn.vnns.io/VTC3/playlist.m3u8
#EXTINF:-1 tvg-id="vtc2" group-title="Kênh VTC | VTC now" tvg-logo="https://s3.amazonaws.com/studiopro-app-vtc/assets/images/vtc2_thumbnail.jpg" type="stream",VTC2 HD
https://vtc130121.cdn.vnns.io/VTC2/playlist.m3u8
#EXTINF:-1 tvg-id="vtc3hd" group-title="Kênh VTC | VTC now" tvg-logo="https://s3.amazonaws.com/studiopro-app-vtc/assets/images/vtc3_thumbnail.jpg" type="stream",VTC3 HD
https://vtc130121.cdn.vnns.io/VTC3/playlist.m3u8
#EXTINF:-1 tvg-id="vtc4hd" group-title="Kênh VTC | VTC now" tvg-logo="https://s3.amazonaws.com/studiopro-app-vtc/assets/images/vtc4_thumbnail.jpg" type="stream",VTC4 HD
https://vtc130121.cdn.vnns.io/VTC4/playlist.m3u8
#EXTINF:-1 tvg-id="vtc5hd" group-title="Kênh VTC | VTC now" tvg-logo="https://s3.amazonaws.com/studiopro-app-vtc/assets/images/vtc5_thumbnail.jpg" type="stream",VTC5 HD
https://vtc130121.cdn.vnns.io/VTC5/playlist.m3u8
#EXTINF:-1 tvg-id="vtc6hd" group-title="Kênh VTC | VTC now" tvg-logo="https://s3.amazonaws.com/studiopro-app-vtc/assets/images/vtc6_thumbnail.jpg" type="stream",VTC6 HD
https://vtc130121.cdn.vnns.io/VTC6/playlist.m3u8
#EXTINF:-1 tvg-id="vtc7hd" group-title="Kênh VTC | VTC now" tvg-logo="https://s3.amazonaws.com/studiopro-app-vtc/assets/images/vtc7_thumbnail.jpg" type="stream",VTC7 HD - Today TV 
https://vtc130121.cdn.vnns.io/VTC7/playlist.m3u8
#EXTINF:-1 tvg-id="vtv8" group-title="Kênh VTC | VTC now" tvg-logo="https://s3.amazonaws.com/studiopro-app-vtc/assets/images/vtc8_thumbnail.jpg" type="stream",VTC8 HD
https://vtc130121.cdn.vnns.io/VTC8/playlist.m3u8
#EXTINF:-1 tvg-id="vtc9hd" group-title="Kênh VTC | VTC now" tvg-logo="https://s3.amazonaws.com/studiopro-app-vtc/assets/images/vtc9_thumbnail.jpg" type="stream",VTC9 HD
https://vtc130121.cdn.vnns.io/VTC9_abr/vtc130121/VTC9_1080p/playlist.m3u8
#EXTINF:-1 tvg-id="vtc10hd" group-title="Kênh VTC | VTC now" tvg-logo="https://s3.amazonaws.com/studiopro-app-vtc/assets/images/vtc10_thumbnail.jpg" type="stream",VTC10 HD
https://vtc130121.cdn.vnns.io/VTC10/playlist.m3u8
#EXTINF:-1 tvg-id="vtc11" group-title="Kênh VTC | VTC now" tvg-logo="https://s3.amazonaws.com/studiopro-app-vtc/assets/images/vtc11_thumbnail.jpg" type="stream",VTC11 HD
https://vtc130121.cdn.vnns.io/VTC11/playlist.m3u8
#EXTINF:-1 tvg-id="vtc12" group-title="Kênh VTC | VTC now" tvg-logo="https://s3.amazonaws.com/studiopro-app-vtc/assets/images/vtc12_thumbnail.jpg" type="stream",VTC12 HD
https://vtc130121.cdn.vnns.io/VTC12/playlist.m3u8
#EXTINF:-1 tvg-id="vtc13hd" group-title="Kênh VTC | VTC now" tvg-logo="https://s3.amazonaws.com/studiopro-app-vtc/assets/images/vtc13_thumbnail.jpg" type="stream",VTC13 HD
https://vtc130121.cdn.vnns.io/VTC13/playlist.m3u8
#EXTINF:-1 tvg-id="vtc13hd" group-title="Kênh VTC | VTC now" tvg-logo="https://portal.vtc.gov.vn/site/img/vtc4k_thumbnail.jpg" type="stream",VTC13 4K
http://vcdn1.vtc.gov.vn:1935/m_4k/smil:4k.smil/playlist.m3u8
#EXTINF:-1 tvg-id="vtc14hd" group-title="Kênh VTC | VTC now" tvg-logo="https://s3.amazonaws.com/studiopro-app-vtc/assets/images/vtc14_thumbnail.jpg" type="stream",VTC14 HD
https://vtc130121.cdn.vnns.io/VTC14_abr/playlist.m3u8
#EXTINF:-1 tvg-id="vtc16" group-title="Kênh VTC | VTC now" tvg-logo="https://s3.amazonaws.com/studiopro-app-vtc/assets/images/vtc16_thumbnail.jpg" type="stream",VTC16 HD
https://vtc130121.cdn.vnns.io/VTC16_abr/vtc130121/VTC16_1080p/chunks.m3u8
#EXTINF:-1 tvg-id="htv1" tvg-logo="https://img.hplus.com.vn/355x200/poster/2018/07/16/185783-505482-HTV1.png" group-title="Kênh HTV" ,HTV1
https://livecdn.fptplay.net/sdb/htv1_hls.smil/chunklist_b2500000.m3u8
#EXTINF:-1 tvg-id="htv2hd" tvg-logo="https://img.hplus.com.vn/355x200/poster/2018/06/05/904719-HTV2HD.png" group-title="Kênh HTV" ,HTV2 HD HTVC 
https://htv-drm-live-cdn.fptplay.net/CDN-FPT02/HTV2-HD-1080p/playlist.m3u8
#EXTINF:-1 tvg-id="htv2hd" tvg-logo="https://img.hplus.com.vn/355x200/poster/2018/06/05/904719-HTV2HD.png" group-title="Kênh HTV" ,HTV2 HD VieON
http://gg.gg/htv2vieon
#EXTINF:-1 tvg-id="htv2hd" tvg-logo="https://img.hplus.com.vn/355x200/poster/2018/06/05/904719-HTV2HD.png" group-title="Kênh HTV" catchup="append" catchup-days="0.3" catchup-source="https://htvc271120.cdn.vnns.io/06b93ec20336126a28dd0872a68932901632397465/htv2.cat.720p.tms/chunks_dvr_range-${start}-3000.m3u8" ,HTV2 HD FPT Play
https://livecdn.fptplay.net/hda1/htv2hd_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 tvg-id="htv3" tvg-logo="https://img.hplus.com.vn/355x200/poster/2018/06/05/750643-HTV3.png" group-title="Kênh HTV" ,HTV3 - DreamsTV
https://htv-drm-live-cdn.fptplay.net/CDN-FPT02/HTV3-SD-480p/chunks.m3u8
#EXTINF:-1 tvg-id="htvkey" tvg-logo="https://img.hplus.com.vn/355x200/poster/2018/08/14/359584-htv-key-web.png" group-title="Kênh HTV" ,HTV Key
https://livecdn.fptplay.net/sdb/htv4_hls.smil/chunklist_b2500000.m3u8
#EXTINF:-1 tvg-id="htv7hd" tvg-logo="https://img.hplus.com.vn/460x260/poster/2018/07/16/928755-665121-HTV7HD.png" group-title="Kênh HTV" catchup="append" catchup-days="0.3" catchup-source="https://htvc271120.cdn.vnns.io/9e4c1bcff9fbfc9480f7cbbfed485cba1632397465/htv7.cat.720p.tms/chunks_dvr_range-${start}-2400.m3u8" ,HTV7 HD FPT Play
https://livecdn.fptplay.net/hda1/htv7hd_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 tvg-id="htv7hd" tvg-logo="https://img.hplus.com.vn/460x260/poster/2018/07/16/928755-665121-HTV7HD.png" group-title="Kênh HTV" ,HTV7 HD VieON
http://gg.gg/htv7vieon
#EXTINF:-1 tvg-id="htv9hd" tvg-logo="https://img.hplus.com.vn/460x260/poster/2018/07/16/422430-665121-HTV9HD.png" group-title="Kênh HTV" catchup="append" catchup-days="0.3" catchup-source="https://htvc271120.cdn.vnns.io/cb40af69a22267aa9177c35ee0a30ec81632397465/htv9.cat.720p.tms/chunks_dvr_range-${start}-5400.m3u8 ,HTV9 HD FPT Play
https://livecdn.fptplay.net/hda1/htv9hd_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 tvg-id="htv9hd" tvg-logo="https://img.hplus.com.vn/460x260/poster/2018/07/16/422430-665121-HTV9HD.png" group-title="Kênh HTV" ,HTV9 HD VieON
http://gg.gg/htv9vieon
#EXTINF:-1 tvg-id="" tvg-logo="https://img.hplus.com.vn/355x200/poster/2018/07/16/546898-111250-HTVTT.png" group-title="Kênh HTV",HTV Thể Thao
https://live-vthcm.vieon.vn/htv_drm/live/htv_the_thao/TV_HD/htv_the_thao_1080p/chunks.m3u8
#EXTINF:-1 tvg-id="htvc_coop" tvg-logo="https://img.hplus.com.vn/355x200/poster/2018/06/05/402721-HTVCoop.png" group-title="Kênh HTV",HTV CO.OP
https://htv-drm-live-cdn.fptplay.net/CDN-FPT02/HTVCOOP-SD-ABR/playlist.m3u8
#EXTINF:-1 tvg-id="htvcthuanviet" tvg-logo="https://img.hplus.com.vn/355x200/poster/2018/06/05/504279-ThuanViet.png" group-title="Kênh HTVC",HTVC Thuần Việt SD
https://htv-drm-live-cdn.fptplay.net/CDN-FPT02/HTVC-THUANVIET-HD-1080p/playlist.m3u8
#EXTINF:-1 tvg-id="htvcthuanviethd" tvg-logo="https://img.hplus.com.vn/355x200/poster/2018/06/05/136820-ThuanVietHD1.png" group-title="Kênh HTVC",HTVC Thuần Việt HD
https://htv-drm-live-cdn.fptplay.net/CDN-FPT02/HTVC-THUANVIETHD-HD-1080p/playlist.m3u8
#EXTINF:-1 tvg-id="htvccanhachd" tvg-logo="http://htvc.vn/uploads/editor/images/Ca%20nhac-01.png" group-title="Kênh HTVC",HTVC Ca Nhạc
https://htv-drm-live-cdn.fptplay.net/CDN-FPT02/HTVC-CANHAC-HD-1080p/playlist.m3u8
#EXTINF:-1 tvg-id="htvcphimhd" tvg-logo="https://img.hplus.com.vn/355x200/poster/2018/06/05/591916-pHIM.png" group-title="Kênh HTVC",HTVC Phim HD
https://htv-drm-live-cdn.fptplay.net/CDN-FPT02/HTVC-PHIM-HD-1080p/playlist.m3u8
#EXTINF:-1 tvg-id="htvcphunuhd" tvg-logo="https://img.hplus.com.vn/355x200/poster/2018/06/05/143922-pn.png" group-title="Kênh HTVC",HTVC Phụ Nữ
https://htv-drm-live-cdn.fptplay.net/CDN-FPT02/HTVC-PHUNU-HD-1080p/playlist.m3u8
#EXTINF:-1 tvg-id="htvcgiadinhhd" tvg-logo="https://img.hplus.com.vn/460x260/poster/2018/06/05/866192-Gia-Dinh.png" group-title="Kênh HTVC",HTVC Gia Đình
https://htv-drm-live-cdn.fptplay.net/CDN-FPT02/HTVC-GIADINH-HD-1080p/playlist.m3u8
#EXTINF:-1 tvg-id="htvcdulichhd" tvg-logo="http://htvc.vn/uploads/channel/2015/02/12/9681507-logo-htvc-dulic.png" group-title="Kênh HTVC",HTVC Du Lịch & Cuộc Sống
https://htv-drm-live-cdn.fptplay.net/CDN-FPT02/HTVC-DULICH-HD-1080p/playlist.m3u8
#EXTINF:-1 tvg-id="htvcfbnchd" tvg-logo="https://img.hplus.com.vn/355x200/poster/2018/06/05/906484-FBNC.png" group-title="Kênh HTVC",HTVC FBNC
https://htv-drm-live-cdn.fptplay.net/CDN-FPT02/FBNC-HD-1080p/playlist.m3u8
#EXTINF:-1 tvg-logo="https://img.hplus.com.vn/460x260/poster/2018/08/02/451568-logo_htvc_shopping.png" group-title="Kênh HTVC",HTVC VGS Shop
https://htv-drm-live-cdn.fptplay.net/CDN-FPT02/HOMESHOPPING-SD-ABR/HTV-ABR/HOMESHOPPING-SD-720p/playlist.m3u8
#EXTINF:-1 tvg-id="htvcplushd" tvg-logo="http://htvc.vn/uploads/editor/images/CPlusLogo_Final.jpg" group-title="Kênh HTVC",HTVC + HD
https://htv-drm-live-cdn.fptplay.net/CDN-FPT02/HTVC-PLUS-HD-1080p/playlist.m3u8
#EXTINF:-1 tvg-id="antvhd" tvg-logo="https://mytv.com.vn/upload/channel/35.png" group-title="Kênh THỜI SỰ & CHÍNH LUẬN " ,ANTV HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://livecdn.fptplay.net/hda2/anninhtv_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 tvg-id="qpvnhd" tvg-logo="https://mytv.com.vn/upload/channel/127.png" group-title="Kênh THỜI SỰ & CHÍNH LUẬN " ,QPVN
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://livecdn.fptplay.net/hda1/quocphongvnhd_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 tvg-id="nhandan" tvg-logo="https://mytv.com.vn/upload/channel/128.png" group-title="Kênh THỜI SỰ & CHÍNH LUẬN " ,NHÂN DÂN HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://video.nhandan.thienvietjsc.net/live/nhandan720/chunklist.m3u8
#EXTINF:-1 tvg-id="ttxvnhd" tvg-logo="https://mytv.com.vn/upload/channel/133.png" group-title="Kênh THỜI SỰ & CHÍNH LUẬN " ,VNEWS - Truyền hình TTXVN
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://livecdn.fptplay.net/hda2/ttxvn_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 tvg-id="quochoi" tvg-logo="https://mytv.com.vn/upload/channel/71.png" group-title="Kênh THỜI SỰ & CHÍNH LUẬN " ,QUỐC HỘI
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
http://113.164.225.140:1935/live/quochoitvlive.stream/playlist.m3u8
#EXTINF:-1 tvg-id="vovtvhd" tvg-logo="https://static.mediacdn.vn/vovTV/web_images/logovov02112020_nobg.png" group-title="Kênh THỜI SỰ & CHÍNH LUẬN " ,VOV TV
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
http://cdn.vovtv.mediatech.vn/vovlive/tv1live.m3u8
#EXTINF:-1 tvg-id="vinhlong1hd" tvg-logo="https://mytv.com.vn/upload/channel/24.png" group-title="Kênh THVL" catchup="append" catchup-days="0.3" catchup-source="https://live1.thvli.vn/-eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmkiOiIvdGh2bDEtNzIwcCIsImV4cCI6MTYzMTg5NzI0MH0.uNJPhwOve1YdUwz6m4RPhE8_tml5LpFPnDz46kTDvBw-/thvl1-720p/chunks_dvr_range-${start}-2760.m3u8" ,THVL1 HD 
https://livecdn.fptplay.net/hda1/vinhlong1_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 tvg-id="vinhlong2hd" tvg-logo="https://mytv.com.vn/upload/channel/28.png" group-title="Kênh THVL" catchup="append" catchup-days="0.3" catchup-source="https://live1.thvli.vn/-eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmkiOiIvdGh2bDItNzIwcCIsImV4cCI6MTYzMTg5NzUwOX0.H-0qQ0vi85SUOJpX-gbTTUijHvcEHbGhEmBMfIFZqnE-/thvl2-720p/playlist_dvr_range-${start}-2700.m3u8" ,THVL2 HD 
https://livecdn.fptplay.net/hda2/vinhlong2_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 tvg-id="vinhlong3hd" tvg-logo="https://mytv.com.vn/upload/channel/29.png" group-title="Kênh THVL" catchup="append" catchup-days="0.3" catchup-source="https://live1.thvli.vn/-eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmkiOiIvdGh2bDMtNzIwcCIsImV4cCI6MTYzMTg5ODAxOH0.3sjlofVodMaFu-ZwLIUvTD-eZhMZvdoTD5IGLxoDlZ8-/thvl3-720p/playlist_dvr_range-${start}-2699.m3u8" ,THVL3 HD
https://livecdn.fptplay.net/hda2/vinhlong3_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 tvg-id="vinhlong4hd" tvg-logo="https://mytv.com.vn/upload/channel/57.png" group-title="Kênh THVL" catchup="append" catchup-days="0.3" catchup-source="https://live1.thvli.vn/-eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmkiOiIvdGh2bDQtNzIwcCIsImV4cCI6MTYzMTg5ODA0OH0.ZVpAeEqyRh1eIv9w1l8gTU46FbbbcE6U9zGtS07xizo-/thvl4-720p/playlist_dvr_range-${start}-1138.m3u8" ,THVL4 HD
https://livecdn.fptplay.net/hda3/vinhlong4hd_hls.smil/chunklist_b2500000.m3u8

#EXTINF:-1 tvg-id="mtvhd" tvg-logo="http://mtvwe.com/images/logo.png?r=12413" group-title="Kênh MUSIC" , MTV Việt Nam HD
https://livecdn.fptplay.net/sdb/mtv_hls.smil/chunklist_b2500000.m3u8
#EXTINF:-1 tvg-logo="https://chungplay.github.io/logo/kpopsexy.png" group-title="Kênh MUSIC" ,Sexy Kpop TV
https://srv1.zcast.com.br/kpoptv/kpoptv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://logos-download.com/wp-content/uploads/2020/06/1HD_Music_Television_Logo.png" group-title="Kênh MUSIC" ,1HD Music
http://1hdru-hls-otcnet.cdnvideo.ru/onehdmusic/tracks-v1a1/index.m3u8
#EXTINF:-1 tvg-logo="https://static.wikia.nocookie.net/tvfan/images/5/57/1920px-VIVA_Logo_1993-1998.png" group-title="Kênh MUSIC" ,VIVA Russia
http://195.9.195.19:8001/hls2/vivarussia/index.m3u8



#EXTINF:-1 tvg-id="channelvhd" tvg-logo="http://htvc.vn/uploads/editor/images/Logo%20Kenh/logo_channelV_422x278.png" group-title="Kênh MUSIC" ,Channel [V] HD 
http://htv-drm-live-cdn.fptplay.net/CDN-FPT02/CHANNELV-HD-1080p/playlist.m3u8
#EXTINF:-1 tvg-id="hbohd-asia"  tvg-logo="https://upload.wikimedia.org/wikipedia/commons/6/67/HBO_New_Logo.png"  group-title="Kênh HBO GO",HBO Asia
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://liveorigin01.hbogoasia.com:8443/origin/live/main/HBO/index.m3u8 
#EXTINF:-1 tvg-id="hbofamilyhd-asia"  tvg-logo="https://upload.wikimedia.org/wikipedia/en/thumb/d/d2/HBO_Family_Asia_logo.svg/200px-HBO_Family_Asia_logo.svg.png"  group-title="Kênh HBO GO",HBO Family Asia
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://liveorigin01.hbogoasia.com:8443/origin/live/main/FAMILY/index.m3u8
#EXTINF:-1 tvg-id="hbohitshd-asia"  tvg-logo="https://upload.wikimedia.org/wikipedia/en/thumb/f/fc/HBOHits-ASIA.png/185px-HBOHits-ASIA.png"  group-title="Kênh HBO GO",HBO HITS Asia
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://liveorigin01.hbogoasia.com:8443/origin/live/main/HITS/index.m3u8
#EXTINF:-1 tvg-id="hbosignaturehd-asia"  tvg-logo="https://upload.wikimedia.org/wikipedia/commons/a/af/HBO_Signature_Asia.png"  group-title="Kênh HBO GO",HBO Signature Asia
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://liveorigin01.hbogoasia.com:8443/origin/live/main/SIG/index.m3u8
#EXTINF:-1 tvg-id="hbofamilyhd-asia"  tvg-logo="https://static.wikia.nocookie.net/logopedia/images/f/f0/611-cinemax.png/revision/latest/scale-to-width-down/200?cb=20200402195206"  group-title="Kênh HBO GO",Cinemax Asia
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://liveorigin01.hbogoasia.com:8443/origin/live/main/MAX/index.m3u8
#EXTINF:-1 tvg-id="hbohd"  tvg-logo="https://upload.wikimedia.org/wikipedia/commons/6/67/HBO_New_Logo.png"  group-title="Kênh MOVIES"  ,HBO Việt Nam
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://livecdn.fptplay.net/hda1/hbo_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 tvg-id="cinemaxhd" tvg-logo="https://qnet.com.vn/data/banners/rci1588038734.png"  group-title="Kênh MOVIES" ,Cinemax Việt Nam
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://livecdn.fptplay.net/hda1/cinemax_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 tvg-id="axnhd" tvg-logo="https://mytv.com.vn/upload/channel/177.png" group-title="Kênh MOVIES" , AXN Việt Nam
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
http://livecdn.fptplay.net/hda3/axnhd_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 tvg-id="warnertvhd" tvg-logo="https://imgur.com/9qJI1Mg.png" group-title="Kênh MOVIES" , Warner Bros. TV HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://livecdn.fptplay.net/hda3/warnertv_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 tvg-id="kix" tvg-logo="http://console.celestialtiger.com/images/upload/693c8d81ab95b24b2549a1d9832efd42b6ff8e6c.png" group-title="Kênh MOVIES" , KIX HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://livecdn.fptplay.net/hda1/kixhd_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 tvg-id="cinemaworldhd" tvg-logo="https://qnet.com.vn/data/banners/hxa1379060076.png" group-title="Kênh MOVIES" ,CinemaWorld HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://livecdn.fptplay.net/hda2/cinemawork_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 tvg-id="hits" tvg-logo="https://www.hitstv.com/img/hits-movies-logo.png" group-title="Kênh MOVIES" ,HITS HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
http://103.195.238.226/hits/mpegts
#EXTINF:-1 tvg-logo="https://www.axn-asia.com/sites/axn-asia.com/files/axn_new.png" group-title="Kênh MOVIES" ,AXN Asia HD 
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://feed.play.mv/live/10005200/MKj28KXjmn/master.m3u8
#EXTINF:-1 tvg-logo="https://chungplay.github.io/logo/hallmarkchannel.png" group-title="Kênh MOVIES",Hallmark Channel TV
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://dai2.xumo.com/amagi_hls_data_xumo1212A-rokuhallmark/CDN/playlist.m3u8
#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/en/1/12/%26flix_logo.png" group-title="Kênh MOVIES",&flix HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://f8e7y4c6.ssl.hwcdn.net/andflixhd/playlist.m3u8
#EXTINF:-1 tvg-logo="https://chungplay.github.io/logo/andpriveHD.png" group-title="Kênh MOVIES",&privé HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://f8e7y4c6.ssl.hwcdn.net/andprivehd/playlist.m3u8


#EXTINF:-1 tvg-id="animaxhd" tvg-logo="https://www.animax-asia.com/sites/animax-asia.com/files/logos/animax-logo_0.png" group-title="Kênh KIDS & CARTOON",Animax HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://livecdn.fptplay.net/hda3/animaxport_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 tvg-id="animaxhd" tvg-logo="https://www.animax-asia.com/sites/animax-asia.com/files/logos/animax-logo_0.png" group-title="Kênh KIDS & CARTOON",Animax Asia
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://feed.play.mv/live/10005200/isU48qPZqV/master.m3u8
#EXTINF:-1 tvg-id="boomerang" tvg-logo="http://mod.cht.com.tw/img/channel/channelpic/102.png" group-title="Kênh KIDS & CARTOON",Boomerang
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://livecdn.fptplay.net/hda3/boomerang_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 tvg-id="cbeebies"  tvg-logo="http://mod.cht.com.tw/img/channel/channelpic/108.png?rand=246" group-title="Kênh KIDS & CARTOON",BBC Cbeebies
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://livecdn.fptplay.net/hda3/cbeebies_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 tvg-id="cartoonhd" tvg-logo="https://chungplay.github.io/logo/cartoonnetwork.png" group-title="Kênh KIDS & CARTOON", Cartoon Network HD 
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://livecdn.fptplay.net/hda3/cartoonnetworkhd_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 tvg-id="babytvhd" tvg-logo="https://www.babytv.com/app/uploads/2019/12/LogoBabyTV-2019.png" group-title="Kênh KIDS & CARTOON",BabyTV HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://livecdn.fptplay.net/hda3/babytvhd_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 tvg-id="babyfirst" tvg-logo="https://chungplay.github.io/logo/babyfirsttv.png" group-title="Kênh KIDS & CARTOON",Baby First HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
http://livecdn.fptplay.net/hda1/babyfirst_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 tvg-id="dreamworks" tvg-logo="http://www.dreamworks-asia.com/images/dwalogo.png" group-title="Kênh KIDS & CARTOON",DreamWorks HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://livecdn.fptplay.net/hda3/dreamworks_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 tvg-id="davinci" tvg-logo="https://chungplay.github.io/logo/davincilogo.png" group-title="Kênh KIDS & CARTOON" type="stream",Da Vinci Kids Learning HD 
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
http://htv-drm-live-cdn.fptplay.net/CDN-FPT02/DAVINCY-HD-1080p/playlist.m3u8
#EXTINF:-1 tvg-id="davinci" tvg-logo="https://chungplay.github.io/logo/disneychannel.png" group-title="Kênh KIDS & CARTOON" type="stream",Disney Channel HD 
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
#https://feed.play.mv/live/10005200/QjZ4g9TmAa/master.m3u8
#EXTINF:-1 tvg-id="davinci" tvg-logo="https://chungplay.github.io/logo/DisneyInternational.png" group-title="Kênh KIDS & CARTOON" type="stream",Disney International HD 
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://feed.play.mv/live/10005200/IegKU9vXWg/master.m3u8
#EXTINF:-1 tvg-logo="https://www.ani-box.com/styles/sky-modern-a1/images/anibox-main-logo-518-140.png" group-title="Kênh KIDS & CARTOON",ANI-BOX
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://56a6b9c3b5417.streamlock.net/livestream/smil:aniboxlive.smil/chunklist_w331817780_b1460000_sltha.m3u8
#EXTINF:-1 tvg-logo="https://chungplay.github.io/logo/contvanime.png" group-title="Kênh KIDS & CARTOON",CONtv Anime
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://dai2.xumo.com/amagi_hls_data_xumo-host-contvanime-junction/CDN/playlist.m3u8
#EXTINF:-1 tvg-logo="https://chungplay.github.io/logo/nick+.png" group-title="Kênh KIDS & CARTOON",Nickelodeon HD +
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://feed.play.mv/live/10005200/s5f1zEMJC1/master.m3u8
#EXTINF:-1 tvg-logo="http://static.epg.best/sa/NickJr.sa.png" group-title="Kênh KIDS & CARTOON",Nickelodeon Junior
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
http://gg.gg/NickelodeonJR
#EXTINF:-1 tvg-logo="https://i0.wp.com/tokusatsunetwork.com/wp-content/uploads/2020/03/tsu-e1584362198575.png" group-title="Kênh KIDS & CARTOON",TokuSHOUTsu
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
http://gg.gg/TokuSHOUTsu

#EXTINF:-1 tvg-id="animalhd" tvg-logo="https://qnet.com.vn/data/banners/rpw1548994974.png" group-title="Kênh QNET" type="stream",Animal Planet HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://livecdn.fptplay.net/hda2/animalplanet_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 tvg-id="afnhd" tvg-logo="http://mod.cht.com.tw/img/channel/channelpic/276.png" group-title="Kênh QNET" type="stream",Asian Food Channel HD - FPT
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://livecdn.fptplay.net/hda1/afchd_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 tvg-id="afnhd" tvg-logo="http://mod.cht.com.tw/img/channel/channelpic/276.png" group-title="Kênh QNET" type="stream",Asian Food Channel HD - HTVC
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
http://htv-drm-live-cdn.fptplay.net/CDN-FPT02/AFC-HD-1080p/playlist.m3u8
#EXTINF:-1 tvg-id="blueantext" tvg-logo="http://mod.cht.com.tw/img/channel/channelpic/383.png" group-title="Kênh QNET" type="stream",ROCK Extreme HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://livecdn.fptplay.net/hda1/blueantext_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:0 tvg-id="blueantent" tvg-logo="http://mod.cht.com.tw/img/channel/channelpic/384.png" group-title="Kênh QNET" type="stream",ROCK Entertainment HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://livecdn.fptplay.net/hda1/blueantent_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 tvg-id="bbcearth" tvg-logo="http://mod.cht.com.tw/img/channel/channelpic/252.png" group-title="Kênh QNET" type="stream",BBC Earth HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://livecdn.fptplay.net/hda2/bbcearth_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 tvg-id="bbclifestyle" tvg-logo="http://mod.cht.com.tw/img/channel/channelpic/260.png" group-title="Kênh QNET" type="stream",BBC Lifestyle HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://livecdn.fptplay.net/sdb/bbclifestyle_2000.stream/chunklist_b2500000.m3u8
#EXTINF:-1 tvg-id="bbcworldnews" tvg-logo="https://upload.wikimedia.org/wikipedia/en/thumb/f/ff/BBC_News.svg/640px-BBC_News.svg.png" group-title="Kênh QNET" type="stream",BBC World News HD 
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://livecdn.fptplay.net/sdb/bbcnew_2000.stream/chunklist_b2500000.m3u8
#EXTINF:-1 tvg-id="cnn" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/CNN.svg/200px-CNN.svg.png" group-title="Kênh QNET" type="stream",CNN HD 
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://livecdn.fptplay.net/sdb/cnn_2000.stream/chunklist_b2500000.m3u8
#EXTINF:-1 tvg-id="dmaxhd" tvg-logo="https://img.hplus.com.vn/355x200/poster/2021/09/30/322227-DMAX-NEW2.png" group-title="Kênh QNET" type="stream",DMAX 
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
http://gg.gg/DMAX720p
#EXTINF:-1 tvg-id="discoveryhd" tvg-logo="https://qnet.com.vn/data/banners/pob1572421124.png" group-title="Kênh QNET" type="stream",Discovery Channel HD - FPT
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://livecdn.fptplay.net/hda2/discovery_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 tvg-id="discoveryhd" tvg-logo="https://qnet.com.vn/data/banners/pob1572421124.png" group-title="Kênh QNET" type="stream",Discovery Channel HD - HTVC
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
http://htv-drm-live-cdn.fptplay.net/CDN-FPT02/DISCOVERY-HD-1080p/playlist.m3u8
#EXTINF:-1 tvg-id="discoveryasiahd" tvg-logo="http://mod.cht.com.tw/img/channel/channelpic/253.png" group-title="Kênh QNET" type="stream",Discovery Asia HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://livecdn.fptplay.net/hda2/discoveryasia_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 tvg-id="davincihd" tvg-logo="https://chungplay.github.io/logo/davincilogo.png" group-title="Kênh QNET" type="stream",Da Vinci Kids Learning HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://livecdn.fptplay.net/hda2/davincihd_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 tvg-id="outdoorfhd" tvg-logo="https://www.outdoorchannel.com/network/img/odc/logo.png" group-title="Kênh QNET" type="stream",Outdoor Channel HD 
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://livecdn.fptplay.net/hda1/outdoorfhd_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 tvg-id="ngchd" tvg-logo="https://www.natgeotv.com/App_Resources2/Themes/2012/Images/Main/natgeo.png" group-title="Kênh QNET" type="stream",National Geographic Channel  HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://livecdn.fptplay.net/hda2/natgeohd_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 tvg-id="ngwhd" tvg-logo="https://www.natgeotv.com/App_Resources2/Themes/2012/Images/Main/natgeowild.png" group-title="Kênh QNET" type="stream",Nat Geo WILD HD - FPT
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://livecdn.fptplay.net/hda3/natgeowild_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 tvg-id="ngwhd" tvg-logo="https://www.natgeotv.com/App_Resources2/Themes/2012/Images/Main/natgeowild.png" group-title="Kênh QNET" type="stream",Nat Geo WILD HD - HTVC
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
http://htv-drm-live-cdn.fptplay.net/CDN-FPT02/NATGEOWILD-HD-1080p/playlist.m3u8
#EXTINF:-1 tvg-id="nhk_world" tvg-logo="https://mytv.com.vn/upload/channel/50.png" group-title="Kênh QNET" type="stream",NHK World Japan HD 
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://livecdn.fptplay.net/hda2/nhkworld_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 tvg-id="tlchd" tvg-logo="https://www.tlc-tw.com/images/logo.png" group-title="Kênh QNET" type="stream",TLC HD - The Learning Channel
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://livecdn.fptplay.net/hda2/travelliving_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 tvg-id="historyhd" tvg-logo="https://chungplay.github.io/logo/history.png" group-title="Kênh QNET" type="stream",History HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
http://gg.gg/History1080p
#EXTINF:-1 tvg-id="fashionhd" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Fashion_TV_logo.svg/250px-Fashion_TV_logo.svg.png" group-title="Kênh QNET" type="stream",Fashion TV HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://livecdn.fptplay.net/hda2/fashiontvhd_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 tvg-id="abcaustralia" tvg-logo="http://fboximages.fptplay.net.vn/Channel/iconChannel/abcaustralia_vdsl.png" group-title="Kênh QNET" type="stream",ABC Australia
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://livecdn.fptplay.net/sdb/australiaplus_hls.smil/chunklist_b2500000.m3u8
#EXTINF:-1 tvg-id="dw" tvg-logo="https://imgstatic.vtvcab.vn/logos/DW_CHANNEL_M.png"  group-title="Kênh QNET" type="stream",DW News HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://livecdn.fptplay.net/hda2/dwenglish_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 tvg-logo="https://chungplay.github.io/logo/cnbc.png" group-title="Kênh QNET" type="stream",CNBC 
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://livecdn.fptplay.net/sdb/cnbc_hls.smil/chunklist_b2500000.m3u8
#EXTINF:-1 tvg-id="arirang" tvg-logo="https://www.arirang.com/images/index/arirang.png" group-title="Kênh QNET" type="stream",Ariang KOREA  TV
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://livecdn.fptplay.net/sdb/arirang_hls.smil/chunklist_b2500000.m3u8
#EXTINF:-1 tvg-id="kbsworld" tvg-logo="https://imgstatic.vtvcab.vn/logos/KBS_WORLD_M.png" group-title="Kênh QNET" type="stream",KBS World HD - FPT
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://vips-livecdn.fptplay.net/hda3/kbs_4000.stream/chunklist.m3u8
#EXTINF:-1 tvg-id="kbsworld" tvg-logo="https://imgstatic.vtvcab.vn/logos/KBS_WORLD_M.png" group-title="Kênh QNET" type="stream",KBS World HD - VieON
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
http://gg.gg/kbsvieon
#EXTINF:-1 tvg-id="bloomberg" tvg-logo="https://mytv.com.vn/upload/channel/184.png" group-title="Kênh QNET" type="stream",Bloomberg TV
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://livecdn.fptplay.net/sdb/bloomberg_hls.smil/chunklist_b2500000.m3u8
#EXTINF:-1 tvg-id="cna" tvg-logo="https://imgstatic.vtvcab.vn/logos/CNA_M.png" group-title="Kênh QNET" type="stream",Channel News Asia
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://livecdn.fptplay.net/sdb/newsasia_hls.smil/chunklist_b2500000.m3u8
#EXTINF:-1 tvg-logo="https://mytv.com.vn/upload/channel/137.png" group-title="Kênh QNET" type="stream",France 24 English
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://livecdn.fptplay.net/sdb/france24_hls.smil/chunklist_b2500000.m3u8
#EXTINF:-1 tvg-id="tv5monde_asie" tvg-logo="https://mytv.com.vn/upload/channel/65.png" group-title="Kênh QNET" type="stream",TV5 Monde Asie
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://livecdn.fptplay.net/sdb/tv5_hls.smil/chunklist_b2500000.m3u8
#EXTINF:-1 tvg-logo="http://www.arirang.com/images/index/arirang.png" group-title="Kênh WORLDWIDE TV" type="stream",Ariang KOREA 
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://amdlive-ch01-ctnd-com.akamaized.net/arirang_1ch/smil:arirang_1ch.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://mytv.com.vn/upload/channel/50.png" group-title="Kênh WORLDWIDE TV" type="stream",NHK World Japan HD Original
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://nhkworld.webcdn.stream.ne.jp/www11/nhkworld-tv/global/2003458/live.m3u8
#EXTINF:-1 tvg-logo="https://imgstatic.vtvcab.vn/logos/CNA_M.png" group-title="Kênh WORLDWIDE TV" type="stream",Channel News Asia HD 
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://d2e1asnsl7br7b.cloudfront.net/7782e205e72f43aeb4a48ec97f66ebbe/index_5.m3u8
#EXTINF:-1 tvg-logo="https://mytv.com.vn/upload/channel/184.png" group-title="Kênh WORLDWIDE TV" type="stream",Bloomberg TV Asia HD 
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://www.bloomberg.com/media-manifest/streams/asia.m3u8
#EXTINF:-1 tvg-logo="https://static.france24.com/meta_og_twcards/jsonld_publisher.png" group-title="Kênh WORLDWIDE TV" type="stream",France 24 HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://static.france24.com/live/F24_FR_HI_HLS/live_tv.m3u8
#EXTINF:-1 tvg-logo="https://www.smithsonianchannel.ca/wp-content/uploads/2018/10/smithsonian-logo-header.png" group-title="Kênh WORLDWIDE TV" type="stream",Smithsonian Channel
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://smithsonianaus-samsungau.amagi.tv/playlist1080p.m3u8
#EXTINF:-1 tvg-logo="https://origin-staticv2.sonyliv.com/masthead_logo/5571681160001.png" group-title="Kênh WORLDWIDE TV" type="stream",Sony BBC Earth HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://feed.play.mv/live/10005200/7EsSDh7aX6/master.m3u8
#EXTINF:-1 tvg-logo="https://chungplay.github.io/logo/food52.png" group-title="Kênh WORLDWIDE TV" type="stream",Food52 TV HD 
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://dai2.xumo.com/amagi_hls_data_xumo1212A-food52/CDN/1280x720_5000000/index.m3u8
#EXTINF:-1 tvg-logo="https://chungplay.github.io/logo/foodnetwork.png" group-title="Kênh WORLDWIDE TV" type="stream",Food Network HD 
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://feed.play.mv/live/10005200/aGu172is5o/master.m3u8
#EXTINF:-1 tvg-logo="https://chungplay.github.io/logo/hgtv.png" group-title="Kênh WORLDWIDE TV" type="stream",HGTV HD - Home and Garden Television
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://feed.play.mv/live/10005200/Wvl02Co4S1/master.m3u8
#EXTINF:-1 tvg-logo="https://www.tlc-tw.com/images/logo.png" group-title="Kênh WORLDWIDE TV" type="stream",TLC HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://feed.play.mv/live/10005200/HE8qFtMl9Q/master.m3u8
#EXTINF:-1 tvg-logo="https://chungplay.github.io/logo/DiscoveryHD.png" group-title="Kênh WORLDWIDE TV" type="stream",Discovery HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://feed.play.mv/live/10005200/2Lkn0sCJBz/master.m3u8
#EXTINF:-1 tvg-logo="https://chungplay.github.io/logo/travelchannel.png" group-title="Kênh WORLDWIDE TV" type="stream",Travel Channel HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://feed.play.mv/live/10005200/2dPCepc9DA/master.m3u8
#EXTINF:-1 tvg-logo="https://www.natgeotv.com/App_Resources2/Themes/2012/Images/Main/natgeopeople.png" group-title="Kênh WORLDWIDE TV" type="stream",Nat Geo People HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
http://58.65.171.202:8000/play/10503/index.m3u8
#EXTINF:-1 tvg-logo="https://chungplay.github.io/logo/history.png" group-title="Kênh WORLDWIDE TV" type="stream",History HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://feed.play.mv/live/10005200/isb9Qf3P5M/master.m3u8
#EXTINF:-1 tvg-logo="https://chungplay.github.io/logo/history2.png" group-title="Kênh WORLDWIDE TV" type="stream",History 2 HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://feed.play.mv/live/10005200/uzBWuYCU0z/master.m3u8
#EXTINF:-1 tvg-logo="https://chungplay.github.io/logo/crimeandinvestigation.png" group-title="Kênh WORLDWIDE TV" type="stream",Crime+ Investigation TV HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://feed.play.mv/live/10005200/37MP1b7MI1/master.m3u8
#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/NASA_logo.svg/574px-NASA_logo.svg.png" group-title="Kênh WORLDWIDE TV" type="stream",NASA TV HD 
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://ntv1.akamaized.net/hls/live/2014075/NASA-NTV1-HLS/master.m3u8
#EXTINF:-1 tvg-logo="https://www.newsmaxtv.com/CMSScripts/NewsmaxTV/images/logos/Newsmax-TV-White.png" group-title="Kênh WORLDWIDE TV" type="stream",Newsmax TV
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://nmxlive.akamaized.net/hls/live/529965/Live_1/index_720.m3u8
https://nmxlive.akamaized.net/hls/live/529965/Live_1/index_1080.m3u8
#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/CBS_News.svg/1200px-CBS_News.svg.png"  group-title="Kênh WORLDWIDE TV" type="stream",CBS NEWS 
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://dai.google.com/linear/hls/event/Sid4xiTQTkCT1SLu6rjUSQ/master.m3u8
#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/TRT_World_logo.svg/640px-TRT_World_logo.svg.png" group-title="Kênh WORLDWIDE TV" type="stream", TRT World HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://tv-trtworld.live.trt.com.tr/master.m3u8
#EXTINF:-1 tvg-logo="https://chungplay.github.io/logo/sbs_viceland.png" group-title="Kênh WORLDWIDE TV" type="stream",SBS Viceland HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://sbs-live.akamaized.net/hls/live/2002828/channel2/open/master_1800K.m3u8
#EXTINF:-1 tvg-logo="https://cdn.one.accedo.tv/files/5e60392da0e845000ffa83eb?sessionKey=01FB9FENYXP3FKNJWMZ5Z9JWHA1178466205#asset" group-title="Kênh WORLDWIDE TV" type="stream",Australia Channel HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://austchannel-live.akamaized.net/hls/live/2002729/austchannel-news/master.m3u8
#EXTINF:-1 tvg-logo="http://static.epg.best/au/ABCNews24.au.png" group-title="Kênh WORLDWIDE TV" type="stream",ABC News 24
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://abc-iview-mediapackagestreams-2.akamaized.net/out/v1/6e1cc6d25ec0480ea099a5399d73bc4b/index.m3u8
#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Deutsche_Welle_Logo.svg/743px-Deutsche_Welle_Logo.svg.png"  group-title="Kênh WORLDWIDE TV" type="stream",DW Deutsch+ 
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://dwamdstream105.akamaized.net/hls/live/2015531/dwstream105/index.m3u8
#EXTINF:-1 tvg-logo="https://ui.cgtn.com/static/ng/resource/images/header_icon/cgtn2020_logo.png" group-title="Kênh WORLDWIDE TV" type="stream",CGTN English
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://live.cgtn.com/1000/prog_index.m3u8
#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/d/d6/CGTN_Documentary_logo.png" group-title="Kênh WORLDWIDE TV" type="stream",CGTN Documentary
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://livedoc.cgtn.com/1000d/prog_index.m3u8
#EXTINF:-1 tvg-logo="https://cdnen.rt.com/static/img/logo.png" group-title="Kênh WORLDWIDE TV" type="stream",RT News HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://rt-glb.gcdn.co/live/rtnews/playlist_4500Kb.m3u8
#EXTINF:-1 tvg-logo="https://rtd.rt.com/s/redesign/pub/img/logo.png" group-title="Kênh WORLDWIDE TV" type="stream",RT Documentary HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://rt-rtd.gcdn.co/live/rtdoc/playlist_4500Kb.m3u8
#EXTINF:-1 tvg-logo="http://i.imgur.com/wzBD6fy.png"  group-title="Kênh WORLDWIDE TV" type="stream",TMZ News
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://dai2.xumo.com/xumocdn/p=roku/amagi_hls_data_xumo1234A-tmz/CDN/1280x720_5000000/index.m3u8
#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Global_News.svg/1200px-Global_News.svg.png" group-title="Kênh WORLDWIDE TV" type="stream",Global News
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://live.corusdigitaldev.com/groupd/live/49a91e7f-1023-430f-8d66-561055f3d0f7/live.isml/live-audio_1=96000-video=2499968.m3u8
#EXTINF:-1 tvg-logo="https://img.nbc.com/sites/nbcunbc/files/images/2020/9/14/NBCNewsNow-Logo-White-344x300.png" group-title="Kênh WORLDWIDE TV" type="stream",NBC News Now 
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://dai2.xumo.com/amagi_hls_data_xumo1212A-xumo-nbcnewsnow/CDN/master.m3u8
#EXTINF:-1 tvg-logo="https://lovenature.com/wp-content/uploads/2020/08/love-nature-logo_peacock.png" group-title="Kênh WORLDWIDE TV" type="stream",LoveNature HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
http://bamus-eng-roku.amagi.tv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://chungplay.github.io/logo/jasmintv.png" group-title="Kênh WORLDWIDE TV" type="stream",Jasmin TV HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
http://109.71.162.112:1935/live/hd.jasminchannel.stream/playlist.m3u8

#EXTINF:-1 group-title="Kênh UHD & 4K" tvg-logo="https://chungplay.github.io/logo/LoveNature4K.png",Love Nature 4K
https://d18dyiwu97wm6q.cloudfront.net/playlist2160p.m3u8
#EXTINF:-1 group-title="Kênh UHD & 4K" tvg-logo="https://mytv.com.vn/upload/channel/162.png",FashionTV UHD
https://fash2043.cloudycdn.services/slive/ftv_ftv_4k_hevc_73d_42080_default_466_hls.smil/playlist.m3u8
#EXTINF:-1 group-title="Kênh UHD & 4K" tvg-logo="https://images.squarespace-cdn.com/content/55f79bede4b0917adab94052/1611005142885-LJJTKDYMQJ7S6SQ8L182/Program-Guide-Channel-Logo_Loupe.png",LOUPE 4K
http://d2dw21aq0j0l5c.cloudfront.net/playlist_3840x2160.m3u8

#EXTINF:-1 tvg-logo="https://mytv.com.vn/upload/channel/190.png" group-title="Kênh VIETNAM LOCAL TV",HN1 HD - Truyền hình Hà Nội
https://live.hanoitv.vn/hntvlive/tv1live.m3u8
#EXTINF:-1 tvg-logo="https://mytv.com.vn/upload/channel/193.png" group-title="Kênh VIETNAM LOCAL TV",HN2 HD - Truyền hình Hà Nội
https://live.hanoitv.vn/hntvlive/tv2live.m3u8
#EXTINF:-1 tvg-logo="https://media.baoquangninh.com.vn/upload/files/logo/logotrangchu1.png" group-title="Kênh VIETNAM LOCAL TV",QTV1 - Truyền hình Quảng Ninh
https://qtv.vncdn.vn/qtvlive/tv1live.m3u8
#EXTINF:-1 tvg-logo="https://media.baoquangninh.com.vn/upload/files/logo/logotrangchu2.png" group-title="Kênh VIETNAM LOCAL TV",QTV3 - Truyền hình Quảng Ninh
https://qtv.vncdn.vn/qtvlive/tv3live.m3u8
#EXTINF:-1 tvg-logo="https://mytv.com.vn/upload/channel/981.png" group-title="Kênh VIETNAM LOCAL TV",BGTV HD - Truyền hình Bắc Giang
https://live.bacgiangtv.vn/bgtvlive/tv1live.m3u8
#EXTINF:-1 tvg-logo="https://mytv.com.vn/upload/channel/892.png" group-title="Kênh VIETNAM LOCAL TV",HYTV  HD - Truyền hình Hưng Yên
https://live.hungyentv.vn/hytvlive/tv1live.m3u8
#EXTINF:-1 tvg-logo="http://laocaitv.vn/lib/images/footer-logo.png" group-title="Kênh VIETNAM LOCAL TV",Truyền hình Lào Cai
http://cdn.3ssoft.vn/livetv/laocaitv/laocaitv/index.m3u8
#EXTINF:-1 tvg-logo="http://yenbaitv.org.vn/modules/frontend/themes/ptthyb/images/logo.png" group-title="Kênh VIETNAM LOCAL TV",Truyền hình Yên Bái
https://yenbaitv.org.vn/hls/livestream.m3u8
#EXTINF:-1 tvg-logo="https://mytv.com.vn/upload/channel/261.png" group-title="Kênh VIETNAM LOCAL TV",STV HD  - Truyền hình Sơn La
http://118.107.85.5:1935/live/smil:STV.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="http://www.langsontv.vn/templates/frontend/lstv/Assets/img/logo_lstv.png" group-title="Kênh VIETNAM LOCAL TV",LSTV HD - Truyền hình Lạng Sơn
http://live.langsontv.vn/lstvlive/tv1live.m3u8
#EXTINF:-1 tvg-logo="https://mytv.com.vn/upload/channel/221.png" group-title="Kênh VIETNAM LOCAL TV",TTV - Truyền hình Tuyên Quang
https://live.tuyenquangtv.vn/hls/ttv.m3u8
#EXTINF:-1 tvg-logo="https://mytv.com.vn/upload/channel/192.png" group-title="Kênh VIETNAM LOCAL TV",PTV - Truyền hình Phú Thọ
https://livecdn.fptplay.net/sda/phutho_2000.stream/chunklist_b2500000.m3u8
#EXTINF:-1 tvg-logo="https://mytv.com.vn/upload/channel/281.png" group-title="Kênh VIETNAM LOCAL TV",HBTV - Truyền hình Hòa Bình
http://hoabinhtvlive.746b3ddb.cdnviet.com/hoabinhtv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://nbtv.vn/templates/frontend/nbtv/Assets/img/logo.png" group-title="Kênh VIETNAM LOCAL TV",Truyền hình Ninh Bình
https://nbtv.vncdn.vn/nbtvlive/tv1live.m3u8
#EXTINF:-1 tvg-logo="https://mytv.com.vn/upload/channel/161.png" group-title="Kênh VIETNAM LOCAL TV",THP HD  - Truyền hình Hải Phòng
https://live.thhp.vn/thp/index.m3u8
#EXTINF:-1 tvg-logo="https://chungplay.github.io/logo/THP+.png" group-title="Kênh VIETNAM LOCAL TV",THP+ HD - Truyền hình Hải Phòng +
https://live.thhp.vn/hls/thpplus/index.m3u8
#EXTINF:-1 tvg-logo="https://mytv.com.vn/upload/channel/992.png" group-title="Kênh VIETNAM LOCAL TV",BTV HD - Truyền hình Bắc Ninh
http://118.107.85.4:1935/live/smil:BTV.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://mytv.com.vn/upload/channel/181.png" group-title="Kênh VIETNAM LOCAL TV",NTV - Truyền hình Nam Định
https://livecdn.fptplay.net/sdc/namdinh_2000.stream/chunklist_b2500000.m3u8
#EXTINF:-1 tvg-logo="http://hanamtv.vn/template/default/images/logo.png" group-title="Kênh VIETNAM LOCAL TV",THHN - Truyền hình Hà Nam
http://117.4.240.220/Medias/HaNam/720P/playlist.m3u8
#EXTINF:-1 tvg-logo="http://vinhphuctv.vn/Portals/4/images/logo-vp.png" group-title="Kênh VIETNAM LOCAL TV",VP HD  - Truyền hình Vĩnh Phúc
http://vinhphuctv.vn:8090/vinhphuclive/web.stream_720p/playlist.m3u8
#EXTINF:-1 tvg-logo="https://mytv.com.vn/upload/channel/251.png" group-title="Kênh VIETNAM LOCAL TV",LTV HD  - Truyền hình Lai Châu 
http://123.31.36.68/live.m3u8?c=vstv361&q=high&type=tv&gcId=1532&userId=&deviceId=&deviceType=&location=NA&requestTime=1586309420781&pkg=pkg11
#EXTINF:-1 tvg-logo="https://mytv.com.vn/upload/channel/271.png" group-title="Kênh VIETNAM LOCAL TV",ĐTV - Truyền hình Điện Biên
https://truyenhinh.vnptvas.vn/live.m3u8?c=vstv362&q=high&type=tv&gcId=1532&userId=&deviceId=&deviceType=&location=NA&requestTime=1586309420781&pkg=pkg11
#EXTINF:-1 tvg-logo="https://mytv.com.vn/upload/channel/111.png" group-title="Kênh VIETNAM LOCAL TV",CRTV - Truyền hình Cao Bằng
http://118.107.85.4:1935/live/smil:CRTV.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://mytv.com.vn/upload/channel/971.png" group-title="Kênh VIETNAM LOCAL TV",TBK - Truyền hình Bắc Kạn HD
https://livecdn.fptplay.net/sdb/backan_hls.smil/chunklist_b2500000.m3u8
#EXTINF:-1 tvg-logo="https://mytv.com.vn/upload/channel/203.png" group-title="Kênh VIETNAM LOCAL TV",TN1 HD - Truyền hình Thái Nguyên
https://streaming.thainguyentv.vn/hls/livestream.m3u8
#EXTINF:-1 tvg-logo="http://thaibinhtv.vn/templates/frontend/tbtv/Assets/img/logo.png" group-title="Kênh VIETNAM LOCAL TV",TBTV HD - Truyền hình Thái Bình
http://cdn.tbtv.mediatech.vn/tbtvlive/tv1live.m3u8
#EXTINF:-1 tvg-logo="https://rsstv.gviet.vn/sctv/157/595/1565944958841.png" group-title="Kênh VIETNAM LOCAL TV",THD SD - Truyền hình Hải Dương
https://livecdn.fptplay.net/sdc/haiduong_2000.stream/chunklist_b2500000.m3u8
#EXTINF:-1 tvg-logo="https://mytv.com.vn/upload/channel/231.png" group-title="Kênh VIETNAM LOCAL TV",HGTV - Truyền hình Hà Giang
http://113.162.84.113:8080/hls/fm/index.m3u8
#EXTINF:-1 tvg-logo="https://mytv.com.vn/upload/channel/361.png" group-title="Kênh VIETNAM LOCAL TV",TTV - Truyền hình Thanh Hóa
http://123.31.36.68/live.m3u8?c=vstv208&q=high&type=tv&token=1111&time=1586395820&gcId=1532&userId=&deviceId=&deviceType=&location=NA&requestTime=1586309420781&pkg=pkg11
#EXTINF:-1 tvg-logo="https://hatinhtv.vn/img/logo-footer.png" group-title="Kênh VIETNAM LOCAL TV",HTTV - Truyền hình Hà Tĩnh
https://hatinhtv.vn/hls/httv.m3u8
#EXTINF:-1 tvg-logo="https://mytv.com.vn/upload/channel/phpKczJ13_5d75cc55e9d4a.png" group-title="Kênh VIETNAM LOCAL TV",Truyền hình Nghệ An
https://live.truyenhinhnghean.vn/hls/na1/index.m3u8
#EXTINF:-1 tvg-logo="http://www.drt.danang.vn/images/drt1.png" group-title="Kênh VIETNAM LOCAL TV",DaNangTV1 - Truyền hình Đà Nẵng
http://drtdnglive.e49a7c38.cdnviet.com/livedrt1/playlist.m3u8
#EXTINF:-1 tvg-logo="http://www.drt.danang.vn/images/drt2.png" group-title="Kênh VIETNAM LOCAL TV",DaNangTV2 - Truyền hình Đà Nẵng
http://drtdnglive.e49a7c38.cdnviet.com/livestream/playlist.m3u8
#EXTINF:1 tvg-logo="https://chungplay.github.io/logo/trthue.png" group-title="Kênh VIETNAM LOCAL TV",TRT - Truyền hình Thừa Thiên Huế
https://live.trt.com.vn/TRT-Online/playlist.m3u8
#EXTINF:-1 tvg-logo="https://img.hplus.com.vn/728x409/banner/2018/06/06/386181-Binh-Thuan.png" group-title="Kênh VIETNAM LOCAL TV",BTV HD - Truyền hình Bình Thuận
http://202.43.109.144:1935/thbttv/bttv/chunklist_w1111614173.m3u8
#EXTINF:-1 tvg-logo="https://lienket.vn/btv6binhthuan" group-title="Kênh VIETNAM LOCAL TV",BTV6 - Truyền hình Bình Thuận
https://livecdn.fptplay.net/sdb/quehuongshop_hls.smil/chunklist_b2500000.m3u8
#EXTINF:-1 tvg-logo="https://mytv.com.vn/upload/channel/851.png" group-title="Kênh VIETNAM LOCAL TV",NTV - Truyền hình Ninh Thuận
https://livecdn.fptplay.net/sda/ninhthuan_2000.stream/chunklist_b2500000.m3u8
#EXTINF:-1 tvg-logo="https://mytv.com.vn/upload/channel/781.png" group-title="Kênh VIETNAM LOCAL TV",PTP - Truyền hình Phú Yên 
https://livecdn.fptplay.net/sda/phuyen_hls.smil/chunklist_b2500000.m3u8
#EXTINF:-1 tvg-logo="http://ktv.org.vn/wp-content/themes/ktv/assets/img/logo.png" group-title="Kênh VIETNAM LOCAL TV",KTV - Truyền hình Khánh Hòa
http://210.245.20.94/hls/ktv1.m3u8
#EXTINF:-1 tvg-logo="https://mytv.com.vn/upload/channel/731.png" group-title="Kênh VIETNAM LOCAL TV",QBTV - Truyền hình Quảng Bình
https://livecdn.fptplay.net/sda/quangbinh_2000.stream/chunklist_b2500000.m3u8
#EXTINF:-1 tvg-logo="https://mytv.com.vn/upload/channel/761.png" group-title="Kênh VIETNAM LOCAL TV",PTQ - Truyền hình Quảng Ngãi
http://118.107.85.5:1935/live/smil:PTQ.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://img.hplus.com.vn/728x409/banner/2018/06/05/443495-QRT.png" group-title="Kênh VIETNAM LOCAL TV",QRT - Truyền hình Quảng Nam
http://113.161.6.157:8081/hls-live/livepkgr/_definst_/liveevent/livestream.m3u8
#EXTINF:-1 tvg-logo="http://brt.vn/common/v1/images/logo-footer.png" group-title="Kênh VIETNAM LOCAL TV",BRT - Truyền hình Bà Rịa Vũng Tàu
https://livecdn.fptplay.net/sdc/bariavungtau_2000.stream/chunklist_b2500000.m3u8
#EXTINF:-1 tvg-logo="https://mytv.com.vn/upload/channel/741.png" group-title="Kênh VIETNAM LOCAL TV",QRTV - Truyền hình Quảng Trị
https://livecdn.fptplay.net/sdc/quangtri_2000.stream/chunklist_b2500000.m3u8
#EXTINF:-1 tvg-logo="http://atv.org.vn/lib/images/logo.png" group-title="Kênh VIETNAM LOCAL TV",ATV - Truyền hình An Giang
http://221.133.9.35:1935/live/1.stream_360p/playlist.m3u8
#EXTINF:-1 tvg-logo="http://www.thtg.vn/wp-content/themes/thtg/images/logo.png" group-title="Kênh VIETNAM LOCAL TV",THTG - Truyền hình Tiền Giang
http://123.25.238.45:1935/live/thtg/playlist.m3u8
#EXTINF:-1 tvg-logo="https://mytv.com.vn/upload/channel/951.png" group-title="Kênh VIETNAM LOCAL TV",HGV - Truyền hình Hậu Giang
https://livecdn.fptplay.net/sda/haugiang_2000.stream/chunklist_b2500000.m3u8
#EXTINF:-1 tvg-logo="http://tayninhtv.vn/public/Home/images/logo_ttv11.png" group-title="Kênh VIETNAM LOCAL TV",TTV11 HD - Truyền hình Tây Ninh
http://202.43.109.142:1935/ttv11/tntv/chunklist_w1452030890.m3u8
#EXTINF:-1 tvg-logo="https://mytv.com.vn/upload/channel/841.png" group-title="Kênh VIETNAM LOCAL TV",THTV - Truyền hình Trà Vinh
https://livecdn.fptplay.net/sdc/travinh_1000.stream/chunklist_b2500000.m3u8
#EXTINF:-1 tvg-logo="https://mytv.com.vn/upload/channel/601.png" group-title="Kênh VIETNAM LOCAL TV", ĐNRTV1 - Truyền hình Đồng Nai
https://livecdn.fptplay.net/sda/dongnai1_2000.stream/chunklist_b2500000.m3u8
#EXTINF:-1 tvg-logo="https://mytv.com.vn/upload/channel/602.png" group-title="Kênh VIETNAM LOCAL TV", ĐNRTV2 - Truyền hình Đồng Nai
https://livecdn.fptplay.net/hda4/dongnai2_2000.stream/chunklist_b2500000.m3u8
#EXTINF:-1 tvg-logo="https://lienket.vn/dn3dongnai" group-title="Kênh VIETNAM LOCAL TV", ĐNRTV3 - Truyền hình Đồng Nai
https://live-vthcm.vieon.vn/htv_drm/live/dong_nai_3/TV_HD/dong_nai_3_480p/playlist.m3u8
#EXTINF:-1 tvg-logo="https://mytv.com.vn/upload/channel/811.png" group-title="Kênh VIETNAM LOCAL TV",THGL HD - Truyền hình Gia Lai
http://113.161.25.3:8134/hls/gialaitv/gialaitv.m3u8
#EXTINF:-1 tvg-logo="https://mytv.com.vn/upload/channel/821.png" group-title="Kênh VIETNAM LOCAL TV",KRT HD - Truyền hình Kon Tum
https://tv.kontumtv.vn/live/kontumtv/kontumtv.m3u8
#EXTINF:-1 tvg-logo="https://mytv.com.vn/upload/channel/481.png" group-title="Kênh VIETNAM LOCAL TV",PTD - Truyền hình DakNong
http://gg.gg/daknongvieon
#EXTINF:-1 tvg-logo="https://mytv.com.vn/upload/channel/471.png" group-title="Kênh VIETNAM LOCAL TV",PTD - Truyền hình DakLak 
https://livecdn.fptplay.net/sdc/daklak_2000.stream/chunklist_b2500000.m3u8
#EXTINF:-1 tvg-logo="https://mytv.com.vn/upload/channel/491.png" group-title="Kênh VIETNAM LOCAL TV",LTV - Truyền hình Lâm Đồng
https://livecdn.fptplay.net/sdc/lamdong_2000.stream/chunklist_b2500000.m3u8
#EXTINF:-1 tvg-logo="https://mytv.com.vn/upload/channel/711.png" group-title="Kênh VIETNAM LOCAL TV",THBT - Truyền hình Bến Tre
http://113.163.94.245/hls-live/livepkgr/_definst_/liveevent/thbt.m3u8
#EXTINF:-1 tvg-logo="https://thbl.vn/wp-content/themes/daith2019/assets/img/logo.png" group-title="Kênh VIETNAM LOCAL TV",BLTV - Truyền hình Bạc Liêu
https://tv.thbl.vn/live/tv/tv.m3u8
#EXTINF:-1 tvg-logo="https://img.hplus.com.vn/460x260/poster/2018/06/18/522019-BTV1.png" group-title="Kênh VIETNAM LOCAL TV",BTV1 HD - Truyền hình Bình Dương
https://livecdn.fptplay.net/hda3/btv1_hls.smil/chunklist_b2500000.m3u8
#EXTINF:-1 tvg-logo="http://img.hplus.com.vn/460x260/poster/2018/06/18/245539-444791-BTV2.png" group-title="Kênh VIETNAM LOCAL TV",BTV2 HD - Truyền hình Bình Dương
https://livecdn.fptplay.net/hda3/btv2_hls.smil/chunklist_b2500000.m3u8
#EXTINF:-1 tvg-logo="https://static.wikia.nocookie.net/logos/images/1/1b/BTV3_HD_logo_2018-2019.png/revision/latest/scale-to-width-down/200?cb=20210124140333&path-prefix=vi" group-title="Kênh VIETNAM LOCAL TV",BTV3 HD - Truyền hình Bình Dương
https://livecdn.fptplay.net/sdb/binhduong3_hls.smil/chunklist_b2500000.m3u8
#EXTINF:-1 tvg-logo="https://static.wikia.nocookie.net/logos/images/7/78/BTV4-0.png/revision/latest?cb=20210122210644&path-prefix=vi" group-title="Kênh VIETNAM LOCAL TV",BTV4 HD - Truyền hình Bình Dương
https://livecdn.fptplay.net/hda2/btv4hd_vhls.smil/chunklist_b2500000.m3u8
#EXTINF:-1 tvg-logo="https://rsstv.gviet.vn/sctv/159/130/1581298778597.png" group-title="Kênh VIETNAM LOCAL TV",An Viên TV(BTV9 HD) - Truyền hình Bình Dương
http://gg.gg/AnVienTV
#EXTINF:-1 tvg-logo="https://i.upanh.org/2020/08/22/NCM_BTV10_logo.png" group-title="Kênh VIETNAM LOCAL TV",BTV10 (NCM) - Truyền hình Bình Dương
https://livecdn.fptplay.net/sda/ncm_2000.stream/chunklist.m3u8
#EXTINF:-1 tvg-logo="http://img.btv.org.vn:81/upload/vod/25032020/1585128658_btv11.png" group-title="Kênh VIETNAM LOCAL TV",BTV11 (Top Home Shopping) - Truyền hình Bình Dương
https://livecdn.fptplay.net/sda/btv11_2000.stream/chunklist.m3u8
#EXTINF:-1 tvg-logo="https://mytv.com.vn/upload/channel/771.png" group-title="Kênh VIETNAM LOCAL TV",BTV - Truyền hình Bình Định
http://truyenhinhbinhdinhonline.dynns.com:8086/live.m3u8
#EXTINF:-1 tvg-logo="https://media.baobinhphuoc.com.vn/upload/files/logo/bptv1.png" group-title="Kênh VIETNAM LOCAL TV",BPTV1 HD - Truyền hình Bình Phước
https://live.baobinhphuoc.com.vn/bptvlive/tv1live.m3u8
#EXTINF:-1 tvg-logo="https://media.baobinhphuoc.com.vn/upload/files/logo/bptv2.png" group-title="Kênh VIETNAM LOCAL TV",BPTV2 HD - Truyền hình Bình Phước
https://live.baobinhphuoc.com.vn/bptvlive/tv2live.m3u8
#EXTINF:-1 tvg-logo="http://thst.vn/Content/images/stv1.png" group-title="Kênh VIETNAM LOCAL TV",STV1 HD - Truyền hình Sóc Trăng
http://113.163.189.104:8135/hls-live/livepkgr/_definst_/liveevent/livestream.m3u8
#EXTINF:-1 tvg-logo="http://thst.vn/Content/images/stv2.png" group-title="Kênh VIETNAM LOCAL TV",STV2 HD - Truyền hình Sóc Trăng
http://113.163.189.104:8135/hls-live/livepkgr/_definst_/liveevent/livestreamstv2.m3u8
#EXTINF:-1 tvg-logo="http://la34.com.vn/wp-content/themes/la34/assets/img/logo.png" group-title="Kênh VIETNAM LOCAL TV",LA34 - Truyền hình Long An
http://113.161.229.13/hls-live/livepkgr/_definst_/liveevent/tv.m3u8
#EXTINF:-1 tvg-logo="https://chungplay.github.io/logo/thdt1.png" group-title="Kênh VIETNAM LOCAL TV",THĐT1 HD - Truyền hình Đồng Tháp
http://202.43.109.142:1935/THDT/thdttv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://chungplay.github.io/logo/thdt2.png" group-title="Kênh VIETNAM LOCAL TV",THDT2 - Truyền hình Đồng Tháp
http://202.43.109.145:1935/thdt2/thdt2/playlist.m3u8
#EXTINF:-1 tvg-logo="https://mytv.com.vn/upload/channel/691.png" group-title="Kênh VIETNAM LOCAL TV",CTV - Truyền hình Cà Mau
http://tv.ctvcamau.vn/live/tv/tv.m3u8
#EXTINF:-1 tvg-logo="https://mytv.com.vn/upload/channel/651.png" group-title="Kênh VIETNAM LOCAL TV",THTPCT - Truyền hình Cần Thơ
https://mekongpassion.com/live/tv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://img.hplus.com.vn/728x409/banner/2018/06/04/894592-KienGiang.png" group-title="Kênh VIETNAM LOCAL TV",KGTV - Truyền hình Kiên Giang 
http://tv.kgtv.vn/live/kgtv/kgtv.m3u8
#EXTINF:-1 tvg-logo="https://mytv.com.vn/upload/channel/683.png" group-title="Kênh VIETNAM LOCAL TV",KGTV1 - Truyền hình Kiên Giang
http://tv.kgtv.vn/live/kgtv1/kgtv1.m3u8
#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/RTHK_TV_31.svg/1200px-RTHK_TV_31.svg.png" group-title="Kênh HONGKONG",RTHK TV 31 (港台電視31)
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://cdn.hkdtmb.com/hls/31/index.m3u8
#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/RTHK_TV_32.svg/1024px-RTHK_TV_32.svg.png" group-title="Kênh HONGKONG",RTHK TV 32 (港台電視32)
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://cdn.hkdtmb.com/hls/32/index.m3u8
#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/RTHK_TV_33.svg/1024px-RTHK_TV_33.svg.png" group-title="Kênh HONGKONG",RTHK TV 33 (港台電視33)
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://cdn.hkdtmb.com/hls/33/index.m3u8
#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/zh/3/3a/HKIBC_logo.png" group-title="Kênh HONGKONG",Hong Kong International Business Channel (香港國際財經台)
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://cdn.hkdtmb.com/hls/76/index.m3u8
#EXTINF:-1 tvg-logo="http://www.hkopentv.com/assets/images/opentv_logo.png" group-title="Kênh HONGKONG",Hong Kong Open TV (香港開電視)
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://cdn.hkdtmb.com/hls/77/index.m3u8
#EXTINF:-1 tvg-logo="https://vignette.wikia.nocookie.net/evchk/images/8/88/Tvb_Jade_cap.png" group-title="Kênh HONGKONG",TVB Jade (翡翠台)
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://cdn.hkdtmb.com/hls/81/index.m3u8
#EXTINF:-1 tvg-logo="https://static.epg.best/hk/TVBJ2.hk.png" group-title="Kênh HONGKONG",TVB J2
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://cdn.hkdtmb.com/hls/82/index.m3u8
#EXTINF:-1 tvg-logo="https://raw.githubusercontent.com/hououinkami/AppleTV/master/ChannelLogo/Hongkong/TVB_News.png" group-title="Kênh HONGKONG",TVB News Channel (無綫新聞台)
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://cdn.hkdtmb.com/hls/83/index.m3u8
#EXTINF:-1 tvg-logo="https://vignette.wikia.nocookie.net/evchk/images/d/d2/TVB_Pearl.png" group-title="Kênh HONGKONG",TVB Pearl (明珠台)
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://cdn.hkdtmb.com/hls/84/index.m3u8
#EXTINF:-1 tvg-logo="https://raw.githubusercontent.com/hououinkami/AppleTV/master/ChannelLogo/Hongkong/TVB_Finance.png" group-title="Kênh HONGKONG",TVB Finance & Information Channel (無綫財經 · 資訊台)
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://cdn.hkdtmb.com/hls/85/index.m3u8
#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/ViuTVsix-logo.svg/1280px-ViuTVsix-logo.svg.png" group-title="Kênh HONGKONG",ViuTVsix
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://cdn.hkdtmb.com/hls/96/index.m3u8
#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/ViuTV_logo.svg/1280px-ViuTV_logo.svg.png" group-title="Kênh HONGKONG",ViuTV
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edge/12.246
https://cdn.hkdtmb.com/hls/99/index.m3u8
#EXTINF:-1  tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/NHK_General_TV_logo.svg/1920px-NHK_General_TV_logo.svg.png" group-title="Kênh JAPAN",NHK総合
http://203.162.235.41:16903
#EXTINF:-1  tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/NHK_Educational_TV_logo.svg/1200px-NHK_Educational_TV_logo.svg.png" group-title="Kênh JAPAN",NHK教育
http://203.162.235.41:16901
#EXTINF:-1  tvg-logo="https://www.nct9.co.jp/wordpress/wp-content/themes/nct/img/service/tv/ch/img_ch_nhkbs1.jpg" group-title="Kênh JAPAN",NHK BS1
http://220.158.149.28:8180/live/TV00000000000000000075@HHZT
#EXTINF:-1  tvg-logo="https://vignette.wikia.nocookie.net/logopedia/images/8/87/Q1_%281%29.jpg" group-title="Kênh JAPAN",NHK BSプレミアム
http://203.162.235.41:16910
#EXTINF:-1  tvg-logo="https://static.epg.best/jp/Asahi1.jp.png" group-title="Kênh JAPAN",テレビ朝日
http://203.162.235.41:16906
#EXTINF:-1  tvg-logo="https://static.epg.best/jp/TVTokyo.jp.png" group-title="Kênh JAPAN",テレビ東京
http://203.162.235.41:16908
#EXTINF:-1  tvg-logo="https://www.abu.org.my/images/articles/news/tbs_logo.jpg" group-title="Kênh JAPAN",TBSテレビ
http://203.162.235.41:16907
#EXTINF:-1  tvg-logo="https://upload.wikimedia.org/wikipedia/en/thumb/e/e9/Fuji_TV_logo.svg/150px-Fuji_TV_logo.svg.png" group-title="Kênh JAPAN",フジテレビ
http://203.162.235.41:16904
#EXTINF:-1  tvg-logo="https://static.epg.best/jp/NipponTV.jp.png" group-title="Kênh JAPAN",日テレ
http://203.162.235.41:16905
#EXTINF:-1  tvg-logo="https://startpoint.jp/wp-content/uploads/fb.jpg" group-title="Kênh JAPAN",日テレNEWS24
https://n24-cdn-live-b.ntv.co.jp/ch01/High.m3u8
#EXTINF:-1  tvg-logo="https://static.epg.best/jp/BSTBS.jp.png" group-title="Kênh JAPAN",BS TBS
http://203.162.235.41:16913
#EXTINF:-1  tvg-logo="https://www.bs-asahi.co.jp/wordpress/wp-content/themes/bs-master/img/no_image.png" group-title="Kênh JAPAN",BS 朝日
http://203.162.235.41:16914
#EXTINF:-1  tvg-logo="https://www.bsfuji.tv/top/common/img/head_logo.png" group-title="Kênh JAPAN",BSフジ
http://203.162.235.41:16911
#EXTINF:-1  tvg-logo="https://www.tv-tokyo.co.jp/information/blog/images/24606404907f11e880a6cbdce0444b13.jpg" group-title="Kênh JAPAN",BS 東京
http://203.162.235.41:16915
#EXTINF:-1  tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/BS4_logo.svg/400px-BS4_logo.svg.png" group-title="Kênh JAPAN",BS 日テレ
http://203.162.235.41:16912
#EXTINF:-1  tvg-logo="https://www.abu.org.my/images/articles/news/tbs_logo.jpg" group-title="Kênh JAPAN",シネフィルWOWOW
http://203.162.235.41:16916
#EXTINF:-1  tvg-logo="https://www.gemtvasia.com/sites/gemtvasia.com/files/logos/logo-small.png" group-title="Kênh JAPAN",GEM TV
http://103.47.132.164/PLTV/88888888/224/3221227187/index.m3u8
#EXTINF:-1 tvg-id="FUJ.JP" tvg-logo="https://tvguide.myjcom.jp/monomedia/ch_logo/otd/logo-7FE4-081-400x400.png" group-title="Kênh JAPAN",Fuji TV (JOCX-DTV)
http://redlabmcdn.s.llnwi.net/jp04/ryowa7hd/playlist.m3u8
#EXTINF:-1 tvg-logo="https://tvguide.myjcom.jp/monomedia/ch_logo/otd/logo-7E87-091-400x400.png" group-title="Kênh JAPAN",Tokyo MX1
https://movie.mcas.jp/switcher/mcas1_2/chunklist.m3u8
#EXTINF:-1 tvg-logo="https://static.wikia.nocookie.net/logopedia/images/1/1d/20150701201731.png/revision/latest/scale-to-width-down/403?cb=20200512214408" group-title="Kênh JAPAN",Tokyo MX2
https://movie.mcas.jp/mcas/mx2_2/chunklist.m3u8
#EXTINF:-1 tvg-logo="https://global.weathernews.com/wp-content/themes/custom-thema/images/common/logo.svg" group-title="Kênh JAPAN",Weather News
https://movie.mcas.jp/mcas/wn1_2/chunklist.m3u8
#EXTINF:-1 tvg-logo="https://static.epg.best/jp/NipponTV.jp.png" group-title="Kênh JAPAN",Nippon TV (JOAX-DTV)
http://redlabmcdn.s.llnwi.net/jp04/ryowa3hd/playlist.m3u8
#EXTINF:-1 tvg-logo="http://www.arirang.com/images/index/arirang.png" group-title="Kênh SOUTH KOREA",Arirang Korea (아리랑 TV)
https://amdlive-ch01-ctnd-com.akamaized.net/arirang_1ch/smil:arirang_1ch.smil/chunklist_b2256000_sleng.m3u8
#EXTINF:-1 tvg-logo="http://img.imbc.com/commons/2018/image/main/mbc-logo.png" group-title="Kênh SOUTH KOREA",MBC HD 
http://vod.mpmbc.co.kr:1935/live/encoder-tv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://image.tving.com/upload/cms/caic/CAIC1600/C00551.png" group-title="Kênh SOUTH KOREA",tVN HD 
http://gg.gg/tVN720p
#EXTINF:-1 tvg-logo="https://image.tving.com/upload/cms/caic/CAIC1600/C01141.png" group-title="Kênh SOUTH KOREA",tvN SHOW HD 
http://gg.gg/tvNSHOW720p
#EXTINF:-1 tvg-logo="https://image.tving.com/upload/cms/caic/CAIC1600/C00579.png" group-title="Kênh SOUTH KOREA",Mnet HD 
http://gg.gg/Mnet720p
#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/KBS_1_logo.svg/640px-KBS_1_logo.svg.png" group-title="Kênh SOUTH KOREA",KBS1 HD
http://kbss.love.sky-media.tk/?id=1
#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/KBS_2_logo.svg/640px-KBS_2_logo.svg.png" group-title="Kênh SOUTH KOREA",KBS2 HD 
http://kbss.love.sky-media.tk/?id=2
#EXTINF:-1 tvg-logo="http://world.kbs.co.kr/service/common/images/kbsworldlogo_png.png" group-title="Kênh SOUTH KOREA",KBS World TV HD 
http://kbss.love.sky-media.tk/?id=3
#EXTINF:-1 tvg-logo="http://www.kbsn.co.kr/images/ch_joy.png" group-title="Kênh SOUTH KOREA",KBS Joy HD
http://kbss.love.sky-media.tk/?id=6
#EXTINF:-1 tvg-logo="http://www.kbsn.co.kr/images/ch_drama.png" group-title="Kênh SOUTH KOREA",KBS Drama HD 
http://kbss.love.sky-media.tk/?id=5
#EXTINF:-1 tvg-logo="http://www.kbsn.co.kr/images/ch_w.png" group-title="Kênh SOUTH KOREA",KBS Story HD 
http://kbss.love.sky-media.tk/?id=8
#EXTINF:-1 tvg-logo="https://news.kbs.co.kr/resources/images/v1/common/logo-txt-24news.png" group-title="Kênh SOUTH KOREA",KBS 24 뉴스 
http://kbss.love.sky-media.tk/?id=4
#EXTINF:-1 tvg-logo="http://www.kbsn.co.kr/images/ch_kids.png" group-title="Kênh SOUTH KOREA", KBS Kids HD
http://kbss.love.sky-media.tk/?id=9
#EXTINF:-1 tvg-logo="http://www.kbsn.co.kr/images/ch_life.png" group-title="Kênh SOUTH KOREA", KBS Life HD 
http://kbss.love.sky-media.tk/?id=7
#EXTINF:-1 tvg-logo="http://www.knn.co.kr/wp-content/themes/knnblog/images/logo.png" group-title="Kênh SOUTH KOREA",KNN - 부산방송
http://211.220.195.200:1935/live/mp4:KnnTV.sdp/playlist.m3u8
#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/4/40/MBN_Channel_Logo.svg/640px-MBN_Channel_Logo.svg.png" group-title="Kênh SOUTH KOREA",MBN - 매일방송
http://origin.flive.skcdn.com/mbn-auth1/1000k/playlist.m3u8
#EXTINF:-1 tvg-logo="https://www.ytn.co.kr/img/comm/logo_ytn_w.png" group-title="Kênh SOUTH KOREA",YTN
http://slive.ytn.co.kr/ytn/_definst_/ytn_stream_20190306/chunklist.m3u8
#EXTINF:-1 tvg-logo="https://image.ytn.co.kr/ytn/replay/ch_logo_4.png" group-title="Kênh SOUTH KOREA",YTN dmb
http://slive.ytn.co.kr:1935/dmb/ydlive_20140419_1/chunklist_w1389588282.m3u8
#EXTINF:-1 tvg-logo="https://static.epg.best/kr/YTNScience.kr.png" group-title="Kênh SOUTH KOREA",YTN Science
http://slive.sciencetv.kr:1935/science/yslive_20140419_1/chunklist_w646673757.m3u8
#EXTINF:-1 tvg-logo="https://image.tving.com/upload/cms/caic/CAIC1700/C01101.png" group-title="Kênh SOUTH KOREA",YTN Life
https://slive.ytn.co.kr/weather/weather_20140419_1/chunklist_w556856077.m3u8
#EXTINF:-1 group-title="Kênh CHINA" tvg-logo="https://uphinh.vn/images/2020/07/01/a891c59491dbeda845d37d02b2df1b5c.png",Truyền hình An Huy (安徽卫视)
http://gg.gg/anhuimac
#EXTINF:-1 group-title="Kênh CHINA" tvg-logo="https://static.ivanti.com/sites/marketing/media/images/logos/customers-color/btv_logo-color.png",Truyền hình Bắc Kinh (北京卫视)
http://gg.gg/beijingmac
#EXTINF:-1 group-title="Kênh CHINA" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/7/7f/DragonTV_logo.png",Truyền hình Thượng Hải (东方卫视)
http://gg.gg/dongfangmac
#EXTINF:-1 group-title="Kênh CHINA" tvg-logo="https://upload.wikimedia.org/wikipedia/en/3/3b/Jiangsu_Broadcasting_Corporation_Logo.png",Truyền hình Giang Tô (江苏卫视)
http://gg.gg/jiangsumac
#EXTINF:-1 group-title="Kênh CHINA" tvg-logo="https://upload.wikimedia.org/wikipedia/zh/6/65/HBTV_logo.png",Truyền hình Hồ Bắc (湖北卫视)
http://gg.gg/hubeimac
#EXTINF:-1 group-title="Kênh CHINA" tvg-logo="https://upload.wikimedia.org/wikipedia/en/6/68/HunanTV_logo.png",Truyền hình Hồ Nam (湖南卫视)
http://gg.gg/hunanmac
#EXTINF:-1 group-title="Kênh CHINA" tvg-logo="https://www.dishpromotions.com/wp-content/uploads/ZTV-logo.png",Truyền hình Chiết Giang (浙江卫视)
http://gg.gg/zhejiangmac
#EXTINF:-1 group-title="Kênh SPORTS" tvg-logo="https://cdn.golfnews.vn/bundles/cmnindex/images/GolfNews_Logo_black.png", Golf New TV HD 
https://884030f97a.vws.vegacdn.vn/live/_definst_/stream_1_a0acb/chunklist.m3u8
#EXTINF:-1 group-title="Kênh SPORTS" tvg-logo="https://chungplay.github.io/logo/sporttv-1.png",SPORT.TV1 HD
http://31.220.41.88:8081/live/pt-sporttv1.stream/playlist.m3u8
#EXTINF:-1 group-title="Kênh SPORTS" tvg-logo="https://chungplay.github.io/logo/sporttv-2.png",SPORT.TV2 HD
http://31.220.41.88:8081/live/pt-sporttv2.stream/playlist.m3u8
#EXTINF:-1 group-title="Kênh SPORTS" tvg-logo="https://chungplay.github.io/logo/sporttv-3.png",SPORT.TV3 HD
http://31.220.41.88:8081/live/pt-sporttv3.stream/playlist.m3u8
#EXTINF:-1 group-title="Kênh SPORTS" tvg-logo="https://chungplay.github.io/logo/sporttv-4.png",SPORT.TV4 HD
http://31.220.41.88:8081/live/pt-sporttv4.stream/playlist.m3u8
#EXTINF:-1 group-title="Kênh SPORTS" tvg-logo="https://chungplay.github.io/logo/sporttv-5.png",SPORT.TV5 HD
http://31.220.41.88:8081/live/pt-sporttv5.stream/playlist.m3u8
#EXTINF:-1 group-title="Kênh SPORTS" tvg-logo="https://www.thesportsdb.com/images/media/logo/RMC_Sport_1.png", RMC SPORT 1 HD
http://pn.tvott.info:80/live/307217171662/307217171662/78380.m3u8
#EXTINF:-1 group-title="Kênh SPORTS" tvg-logo="https://www.thesportsdb.com/images/media/logo/RMC_Sport_2.png",RMC SPORT 2 HD
http://pn.tvott.info:80/live/307217171662/307217171662/78379.m3u8
#EXTINF:-1 group-title="Kênh SPORTS" tvg-logo="https://chungplay.github.io/logo/eleven-sports-1-hd.png",ELEVEN SPORTS 1 HD
http://207.110.52.61:8080/s/hls/5/3570/eleven_sports_1_355/1/1/index.m3u8
#EXTINF:-1 group-title="Kênh SPORTS" tvg-logo="https://chungplay.github.io/logo/eleven-sports-2-hd.png",ELEVEN SPORTS 2 HD
http://207.110.52.61:8080/s/hls/5/9335/eleven_sports_2_303/1/1/index.m3u8
#EXTINF:-1 group-title="Kênh SPORTS" tvg-logo="https://chungplay.github.io/logo/TringSport1.png",Tring Sport 1 HD
http://93.157.62.180/TringSport1HD/index.m3u8
#EXTINF:-1 group-title="Kênh SPORTS" tvg-logo="https://chungplay.github.io/logo/TringSport2.png",Tring Sport 2 HD
http://93.157.62.180/TringSport2HD/index.m3u8
#EXTINF:-1 group-title="Kênh SPORTS" tvg-logo="https://www.tvshqipon.com/wp-content/uploads/2019/06/Super-Sport-1-Live.png", Super Sport 1 HD
http://93.157.62.180/Supersport1/index.m3u8
#EXTINF:-1 group-title="Kênh SPORTS" tvg-logo="https://www.tvshqipon.com/wp-content/uploads/2019/06/Super-Sport-2-Live.png", Super Sport 2 HD
http://93.157.62.180/Supersport2/index.m3u8
#EXTINF:-1 group-title="Kênh SPORTS" tvg-logo="https://www.tvshqipon.com/wp-content/uploads/2019/06/SuperSport-3-Live.png", Super Sport 3 HD
http://93.157.62.180/Supersport3/index.m3u8
#EXTINF:-1 group-title="Kênh SPORTS" tvg-logo="https://i.ibb.co/rcK5Pbj/Ksport1-BEARTV.png", K Sport 1
http://93.157.62.180/KSport1/index.m3u8
#EXTINF:-1 group-title="Kênh SPORTS" tvg-logo="https://i.ibb.co/rcK5Pbj/Ksport1-BEARTV.png", K Sport 2
http://93.157.62.180/KSport2/index.m3u8
#EXTINF:-1 group-title="Kênh SPORTS" tvg-logo="https://www.beinsportsxtra.com/images/icons/logo/beIN-SPORTS-XTRA_LOGO.png",BEIN SPORTS XTRA USA
https://siloh-ns1.plutotv.net/lilo/production/bein/master_1.m3u8
#EXTINF:-1 group-title="Kênh SPORTS" tvg-logo="http://www.talhouk.com/tv/Logos/Canal+_Sport_HD.png",CANAL + SPORTS
http://207.110.52.61:8080/s/hls/5/293/canal_plus_sport_polska_250/1/1/index.m3u8
#EXTINF:-1 group-title="Kênh SPORTS" tvg-logo="https://www.primaplay.ro/assets/imgs/channel/looksportplus.png",LOOK SPORT + HD
https://stream1.1616.ro:1945/lookplus/livestream/chunklist.m3u8
#EXTINF:-1 group-title="Kênh SPORTS" logo="https://chungplay.github.io/logo/RTSHSport.png",RTSH Sport HD
https://tvlive.rtsh.dev/live/sport_ott_p3/playlist.m3u8
#EXTINF:-1 group-title="Kênh SPORTS" tvg-logo="http://onegolftv.com/wp-content/uploads/2018/08/onegolf-HD-with-image-512.png",ONE GOLF HD
http://162.250.201.58:6211/pk/ONEGOLF/index.m3u8
#EXTINF:-1 group-title="Kênh SPORTS" tvg-logo="https://logos-download.com/wp-content/uploads/2016/09/Red_Bull_TV_logo.png",Red Bull TV HD
https://rbmn-live.akamaized.net/hls/live/590964/BoRB-AT/master_6660.m3u8
#EXTINF:-1 group-title="Kênh SPORTS" tvg-logo="http://static.epg.best/gr/EdgeSport.gr.png" , Edge Sports HD 
https://dai.google.com/linear/hls/event/d4zeSI-dTuqizFrByjs3OA/master.m3u8
#EXTINF:-1 group-title="Kênh SPORTS"  tvg-logo="http://static.epg.best/us/Stadium.us.png" , Stadium
https://stadiumlivein-i.akamaihd.net/hls/live/522512/mux_4/master.m3u8
#EXTINF:-1 group-title="Kênh SPORTS"  tvg-logo="https://upload.wikimedia.org/wikipedia/commons/8/82/CBS_Sports_HQ.png" ,CBS Sports HQ
http://dai.google.com/linear/hls/event/9Lq0ERvoSR-z9AwvFS-xYA/master.m3u8
#EXTINF:-1 group-title="Kênh SPORTS"  tvg-logo="https://kokfights.com/wp-content/uploads/2018/05/kok_logo.png" ,KOK Fights HD
https://live-k2301-kbp.1plus1.video/sport/smil:sport.smil/playlist.m3u8
#EXTINF:-1 group-title="Kênh SPORTS"  tvg-logo="https://snagfilms-a.akamaihd.net/cf9c3bbc-917a-4447-90ab-55bf78b01f49/images/83/36/d90134124307b18e251dce2033ad/1566507637959_laximages-tab.png" ,LSN - Lax Sports Network
https://1840769862.rsc.cdn77.org/FTF/LSN_SCTE.m3u8
#EXTINF:-1 group-title="Kênh SPORTS"  tvg-logo="http://admango.cdn.mangomolo.com/analytics/uploads/71/icons/live/dubai-racing-live.png" , Dubai Racing
http://dmisvthvll.cdn.mangomolo.com/events/smil:events.smil/chunklist_b1600000.m3u8
#EXTINF:-1 group-title="Kênh SPORTS" tvg-logo="http://admango.cdn.mangomolo.com/analytics/uploads/71/icons/live/duabi-racing-2-live.png" , Dubai Racing 2
http://dmithrvll.cdn.mangomolo.com/dubairacing/smil:dubairacing.smil/chunklist_b1600000.m3u8
#EXTINF:-1 group-title="Kênh SPORTS" tvg-logo="http://admango.cdn.mangomolo.com/analytics/uploads/71/5bfea86c98.png" , Dubai Racing 3
http://dmithrvll.cdn.mangomolo.com/dubaimubasher/smil:dubaimubasher.smil/playlist.m3u8
#EXTINF:-1 group-title="Kênh SPORTS" tvg-logo="http://static.epg.best/au/RacingCom.au.png" , Racing.com
https://racingvic-i.akamaized.net/hls/live/598695/racingvic/1500.m3u8
#EXTINF:-1 group-title="Kênh SPORTS" tvg-logo="https://media.info/i/lf/300/1514269404/6402.png" ,Sky Racing 1
https://skylivesky-i.akamaihd.net/hls/live/569780/skylive/sky1_extreme@569780.m3u8
#EXTINF:-1 group-title="Kênh SPORTS" tvg-logo="https://media.info/i/lf/300/1514269377/6411.png" ,Sky Racing 2
https://skylivesky-i.akamaihd.net/hls/live/569780/skylive/sky2_extreme@569780.m3u8
#EXTINF:-1 group-title="Kênh SPORTS" tvg-logo="https://i.imgur.com/XakLUm4.png" ,Australian  Sports Channel
https://austchannel-live.akamaized.net/hls/live/2002736/austchannel-sport/master.m3u8
#EXTINF:-1 group-title="Kênh SPORTS" tvg-logo="https://chungplay.github.io/logo/skyracingcentral.png" ,Sky Thoroughbred Central
https://skylivesky-i.akamaihd.net/hls/live/569780/skylive/stcsd_extreme@569780.m3u8
EXTINF:-1 group-title="Kênh SPORTS" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b7/FITE_TV.svg/1200px-FITE_TV.svg.png" ,FITE 24/7 HD
https://cdn-cf.fite.tv/linear/fite247/playlist.m3u8
EXTINF:-1 group-title="Kênh SPORTS" tvg-logo="https://mmajunkie.usatoday.com/wp-content/uploads/sites/91/2017/07/mmaj-header-logo.png",MMA Junkie HD
https://a.jsrdn.com/broadcast/80f6ba72c8/+0000/high/c.m3u8
EXTINF:-1 group-title="Kênh SPORTS" tvg-logo="https://www.flosports.tv/wp-content/uploads/2020/05/FloSports-Secondary-igniteblack.png",MMA TV
https://a.jsrdn.com/broadcast/47cff5378f/+0000/high/c.m3u8
#EXTINF:-1 group-title="Kênh SPORTS" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/7/76/MLS_crest_logo_RGB_gradient.svg/1200px-MLS_crest_logo_RGB_gradient.svg.png" , MLS Soccer TV
https://service-stitcher.clusters.pluto.tv/stitch/hls/channel/5cb626cfcaf83414128f439c/master.m3u8?deviceType=web&deviceMake=Chrome&deviceModel=Chrome&sid=d1634607-2892-447a-b316-17a106f905fb&deviceId=9f228953-21cb-4b82-a393-dd32d047379f&deviceVersion=76.0.3809.132&appVersion=2.7.4-9a7fc53e0c1da468e3c566c3f53e98a36ca1f97b&deviceDNT=0&userId=&advertisingId=&deviceLat=45.4994&deviceLon=-73.5703&app_name=&appName=web&buildVersion=&appStoreUrl=&architecture=&serverSideAds=true
#EXTINF:-1 group-title="Kênh SPORTS" tvg-logo="https://i.ibb.co/4jGtHGt/EXTV-BEARTV.png", Extreme Sports HD 
http://58.65.171.202:8000/play/10506/index.m3u8
#EXTINF:-1 group-title="Kênh SPORTS" tvg-logo="https://i.imgur.com/LS2PSpt.png",EUROSPORT 1
http://37.99.5.234/btv/SWM/Eurosport/Eurosport_576p_2000kbps.m3u8
#EXTINF:-1 group-title="Kênh SPORTS" tvg-logo="https://i.imgur.com/TxipcCK.png",EUROSPORT 2
http://37.99.5.234/btv/SWM/Eurosport2/Eurosport2_576p_2000kbps.m3u8

#EXTINF:-1 group-title ="Kênh BEIN FOOTBALL", VIP AR: Bein Sport FHD1
http://subtv.premuimservers.com:8080/190ph3q4q863kvk5/190ph3q4q863kvk5/27099
#EXTINF:-1 group-title ="Kênh BEIN FOOTBALL", VIP AR: Bein Sport FHD2
http://subtv.premuimservers.com:8080/190ph3q4q863kvk5/190ph3q4q863kvk5/27098
#EXTINF:-1 group-title ="Kênh BEIN FOOTBALL", VIP AR: Bein Sport FHD3
http://subtv.premuimservers.com:8080/190ph3q4q863kvk5/190ph3q4q863kvk5/27097
#EXTINF:-1 group-title ="Kênh BEIN FOOTBALL", VIP AR: Bein Sport FHD4
http://subtv.premuimservers.com:8080/190ph3q4q863kvk5/190ph3q4q863kvk5/27096
#EXTINF:-1 group-title ="Kênh BEIN FOOTBALL", VIP AR: Bein Sport FHD5
http://subtv.premuimservers.com:8080/190ph3q4q863kvk5/190ph3q4q863kvk5/27095
#EXTINF:-1 group-title ="Kênh BEIN FOOTBALL", VIP AR: Bein Sport FHD6
http://subtv.premuimservers.com:8080/190ph3q4q863kvk5/190ph3q4q863kvk5/27094
#EXTINF:-1 group-title ="Kênh BEIN FOOTBALL", VIP AR: Bein Sport FHD7
http://subtv.premuimservers.com:8080/190ph3q4q863kvk5/190ph3q4q863kvk5/27093
#EXTINF:-1 group-title ="Kênh BEIN FOOTBALL", VIP AR: Bein Sport FHD8
http://subtv.premuimservers.com:8080/190ph3q4q863kvk5/190ph3q4q863kvk5/27092
#EXTINF:-1 group-title ="Kênh BEIN FOOTBALL", VIP AR: Bein Sport FHD9
http://subtv.premuimservers.com:8080/190ph3q4q863kvk5/190ph3q4q863kvk5/27091
#EXTINF:-1 group-title ="Kênh BEIN FOOTBALL", VIP AR: Bein Sport FHD10
http://subtv.premuimservers.com:8080/190ph3q4q863kvk5/190ph3q4q863kvk5/27090
#EXTINF:-1 group-title ="Kênh BEIN FOOTBALL", VIP AR: Bein Sport FHD11
http://subtv.premuimservers.com:8080/190ph3q4q863kvk5/190ph3q4q863kvk5/137082
#EXTINF:-1 group-title ="Kênh BEIN FOOTBALL", VIP AR: Bein Sport FHD12
http://subtv.premuimservers.com:8080/190ph3q4q863kvk5/190ph3q4q863kvk5/173442
#EXTINF:-1 group-title ="Kênh BEIN FOOTBALL", VIP AR: Bein Sport FHD13
http://subtv.premuimservers.com:8080/190ph3q4q863kvk5/190ph3q4q863kvk5/137024
#EXTINF:-1 group-title="Kênh Zing MP3 Radio" tvg-logo="https://photo-zmp3.zadn.vn/avatars/8/5/4/0/854010f76bddeefd5f13305a1d6cc8be.jpg", Zing MP3 - On Air
https://multi-playlist-zmp3.zadn.vn/9tPzLPYORS8/zhls/playback-realtime/a07d79b945fcaca2f5ed/index.m3u8
#EXTINF:-1 group-title="Kênh Zing MP3 Radio" tvg-logo="https://photo-zmp3.zadn.vn/avatars/7/7/8/d/778d152062edfbe0e4c4abf151858bf0.jpg", Zing MP3 - Chạm
https://multi-playlist-zmp3.zadn.vn/62YE6lXdY4w/zhls/playback-realtime/db68d4afe8ea01b458fb/index.m3u8
#EXTINF:-1 group-title="Kênh Zing MP3 Radio" tvg-logo="https://photo-zmp3.zadn.vn/avatars/1/4/6/b/146b49d11cc9b3bc591823bfedb8bce2.jpg", Zing MP3 - Vpop
https://multi-playlist-zmp3.zadn.vn/wTSwRIGOON0/zhls/playback-realtime/6eeb692c5569bc37e578/index.m3u8
#EXTINF:-1 group-title="Kênh Zing MP3 Radio" tvg-logo="https://photo-zmp3.zadn.vn/avatars/0/9/9/3/0993b3110c60ba6518fceeba9913d20d.jpg", Zing MP3 - Acoustic
https://multi-playlist-zmp3.zadn.vn/ktkT8IgzcQQ/zhls/playback-realtime/08aae96dd5283c766539/index.m3u8
#EXTINF:-1 group-title="Kênh Zing MP3 Radio" tvg-logo="https://photo-zmp3.zadn.vn/avatars/1/3/0/5/1305cd954d22d89fef4354301613fd68.jpg", Zing MP3 - Bolero
https://multi-playlist-zmp3.zadn.vn/BtRvAOtW5jk/zhls/playback-realtime/e3b9f87ec43b2d65742a/index.m3u8
#EXTINF:-1 group-title="Kênh Zing MP3 Radio" tvg-logo="https://photo-zmp3.zadn.vn/avatars/b/f/3/b/bf3bf87a788a5d0b8719c6feee774a2e.jpg", Zing MP3 - Rap Việt
https://multi-playlist-zmp3.zadn.vn/Itsn5VCb5Uo/zhls/playback-realtime/4f2980eebcab55f50cba/index.m3u8
#EXTINF:-1 group-title="Kênh Zing MP3 Radio" tvg-logo="https://photo-zmp3.zadn.vn/avatars/c/f/2/4/cf2428f7e56a8c2a52d84cb106891de2.jpg", Zing MP3 - Kpop
https://multi-playlist-zmp3.zadn.vn/94rxZ-Dfzro/zhls/playback-realtime/ff294ded71a898f6c1b9/index.m3u8
#EXTINF:-1 group-title="Kênh Zing MP3 Radio" tvg-logo="https://photo-zmp3.zadn.vn/avatars/b/0/d/a/b0da7c8ecd6521337682f3a86fa0170f.jpg", Zing MP3 - USUK
https://multi-playlist-zmp3.zadn.vn/RckDo1XPsU4/zhls/playback-realtime/111c87d8bb9d52c30b8c/index.m3u8



'''
import requests
import os
import sys

windows = False
if 'win' in sys.platform:
    windows = True

def grab(url):
    response = requests.get(url, timeout=15).text
    if '.m3u8' not in response:
        #response = requests.get(url).text
        if '.m3u8' not in response:
            if windows:
                print('https://raw.githubusercontent.com/chungplay/chungplay.github.io/main/assets/chung_na.m3u')
                return
            os.system(f'wget {url} -O temp.txt')
            response = ''.join(open('temp.txt').readlines())
            if '.m3u8' not in response:
                print('https://raw.githubusercontent.com/chungplay/chungplay.github.io/main/assets/chung_na.m3u')
                return
    end = response.find('.m3u8') + 5
    tuner = 100
    while True:
        if 'https://' in response[end-tuner : end]:
            link = response[end-tuner : end]
            start = link.find('https://')
            end = link.find('.m3u8') + 5
            break
        else:
            tuner += 5
    print(f"{link[start : end]}")

print('#EXTM3U url-tvg="http://megavie.live/schedule/epg.xml" tvg-shift=0 cache=500 deinterlace=1 aspect-ratio=16:9 m3uautoload=1')
print(banner)
s = requests.Session()
with open('../URL_link.txt') as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('~~'):
            continue
        if not line.startswith('https:'):
            line = line.split('|')
            ch_name = line[0].strip()
            grp_title = line[1].strip().title()
            tvg_logo = line[2].strip()
            tvg_id = line[3].strip()
            print(f'\n#EXTINF:-1 group-title="{grp_title}" tvg-logo="{tvg_logo}" tvg-id="{tvg_id}", {ch_name}')
        else:
            grab(line)
            
if 'temp.txt' in os.listdir():
    os.system('rm temp.txt')
    os.system('rm watch*')
