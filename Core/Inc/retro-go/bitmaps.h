#pragma once
#include <stdint.h>

typedef struct
{
    uint32_t width;
    uint32_t height;
    const char logo[];
} retro_logo_image;


//extern void odroid_overlay_draw_logo(uint16_t x_pos, uint16_t y_pos, retro_logo_image *logo, uint16_t color);

extern const retro_logo_image logo_rgo;

extern const retro_logo_image logo_flash;

extern const retro_logo_image logo_gnw;

extern const retro_logo_image header_sg1000;
extern const unsigned char logo_sg1000[];

extern const retro_logo_image header_col;
extern const unsigned char logo_col[];

extern const retro_logo_image header_gb;
extern const unsigned char logo_gb[];

extern const retro_logo_image header_gg;
extern const unsigned char logo_gg[];

extern const retro_logo_image header_nes;
extern const unsigned char logo_nes[];

extern const retro_logo_image header_pce;
extern const unsigned char logo_pce[];

extern const retro_logo_image header_sms;
extern const unsigned char logo_sms[];

extern const retro_logo_image header_gw;
extern const unsigned char logo_gw[];
