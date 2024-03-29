-----------------
--- Libraries ---
-----------------

-- If LuaRocks is installed, make sure that packages installed through it are
-- found (e.g. lgi). If LuaRocks is not installed, do nothing.
pcall(require, "luarocks.loader")

-- Standard awesome libraries
local gears = require("gears")
local awful = require("awful")
require("awful.autofocus")

-- Widget and layout library
local wibox = require("wibox")

-- Theme handling library
local beautiful = require("beautiful")

-- Notification library. Use Dunst instead
-- local naughty = require("naughty")

-- Hotkeys help menu
local hotkeys_popup = require("awful.hotkeys_popup")

-- Enable hotkeys help widget for VIM and other apps
-- when client with a matching name is opened:
-- require("awful.hotkeys_popup.keys")


----------------------
--- Error handling ---
----------------------

-- Check if awesome encountered an error during startup and fell back to
-- another config (This code will only ever execute for the fallback config)
if awesome.startup_errors then
    naughty.notify({ preset = naughty.config.presets.critical,
                     title = "You freaked up!",
                     text = awesome.startup_errors })
end

-- Handle runtime errors after startup
do
    local in_error = false
    awesome.connect_signal("debug::error", function (err)
        -- Make sure we don't go into an endless error loop
        if in_error then return end
        in_error = true

        naughty.notify({ preset = naughty.config.presets.critical,
                         title = "Error!",
                         text = tostring(err) })
        in_error = false
    end)
end


---------------------
----- Variables -----
---------------------

-- Themes define colours, icons, font and wallpapers.
beautiful.init("~/.config/awesome/theme.lua")

-- This is used later as the default terminal and editor to run.
terminal          = "kitty"
terminal_floating = "kitty --class floating"
editor            = "vim"
editor_cmd        = terminal .. " -e " .. editor
clock_app         = "gnome-clocks"
calendar_app      = "gnome-calendar"
packages_command  = terminal_floating .. " -e " .. "sudo dnf update"
flatpaks_command  = terminal_floating .. " -e " .. "flatpak update"

-- Default modkey.
-- Usually, Mod4 is the key with a logo between Control and Alt.
-- If you do not like this or do not have such a key,
-- I suggest you to remap Mod4 to another key using xmodmap or other tools.
-- However, you can use another modifier like Mod1, but it may interact with others.
modkey = "Mod4"

-- Table of layouts to cover with awful.layout.inc, order matters.
awful.layout.layouts = {
    awful.layout.suit.tile,
    awful.layout.suit.floating,
    awful.layout.suit.max,
    -- awful.layout.suit.tile.left,
    -- awful.layout.suit.tile.bottom,
    -- awful.layout.suit.tile.top,
    -- awful.layout.suit.fair,
    -- awful.layout.suit.fair.horizontal,
    -- awful.layout.suit.spiral,
    -- awful.layout.suit.spiral.dwindle,
    -- awful.layout.suit.max.fullscreen,
    -- awful.layout.suit.magnifier,
    -- awful.layout.suit.corner.nw,
    -- awful.layout.suit.corner.ne,
    -- awful.layout.suit.corner.sw,
    -- awful.layout.suit.corner.se,
}


------------------
------ Menu ------
------------------

-- Default awesome menu
myawesomemenu = {
   { "Reload", awesome.restart },
   { "Hotkeys", function() hotkeys_popup.show_help(nil, awful.screen.focused()) end },
   { "Configuration", editor_cmd .. " " .. awesome.conffile },
   { "Documentation", "firefox https://awesomewm.org/doc/api/" },
}

-- Power menu
mypowermenu = {
    { "Log out", function() awesome.quit() end },
    { "Shutdown", "shutdown now" },
    { "Reboot", "reboot" },
}

mymainmenu = awful.menu({ items = {
                                    { "Power", mypowermenu     },
                                    { "Awesome", myawesomemenu },
                                    { "Terminal", terminal     }
                                  }
                        })

mylauncher = awful.widget.launcher({ image = beautiful.awesome_icon,
                                     menu = mymainmenu })


-----------------
----- Wibar -----
-----------------

-- Tasklist template to make icons centred
local tasklist_template = {
    {
        nil,
        {
            {
                { widget = wibox.widget.imagebox, id = "icon_role" },
                id     = "icon_margin_role",
                left   = 4,
                top    = 8,
                bottom = 8,
                widget = wibox.container.margin
            },
            {
                {
                    id     = "text_role",
                    widget = wibox.widget.textbox,
                },
                id     = "text_margin_role",
                left   = 6,
                right  = 4,
                widget = wibox.container.margin
            },
            --fill_space = true,
            layout     = wibox.layout.fixed.horizontal
        },
        expand = "outside",
        layout = wibox.layout.align.horizontal,
    },
    id     = "background_role",
    widget = wibox.container.background
}


-- Packages updates
packages_buttons = awful.button({ }, 1, function()
    awful.spawn.easy_async(packages_command, function(out)
        packages_timer:emit_signal("timeout")
    end)
end)

packages_widget, packages_timer = awful.widget.watch(
    "sh -c 'dnf list updates -q | wc -l'",
    1800,
    function(widget, stdout)
        value = tonumber(stdout)
        if value == 0 then
            widget:set_markup("<span foreground='#89b4fa'>Up to date</span>")
        else
            widget:set_markup(string.format("<span foreground='#89b4fa'>%d</span>", value - 1))
            widget:buttons(packages_buttons)
        end
    end)

packages_text = wibox.widget({
        widget = wibox.widget.textbox,
        markup = "<span foreground='#89b4fa'>ﮮ</span>",
        font = beautiful.icons_font,
        buttons = packages_buttons,
    })


-- FLatpaks updates
flatpaks_buttons = awful.button({ }, 1, function()
    awful.spawn.easy_async(flatpaks_command, function(out)
        flatpaks_timer:emit_signal("timeout")
    end)
end)

flatpaks_widget, flatpaks_timer = awful.widget.watch(
    "sh -c 'flatpak remote-ls --updates | wc -l'",
    1800,
    function(widget, stdout)
        value = tonumber(stdout)
        if value == 0 then
            widget:set_markup("<span foreground='#a6e3a1'>Up to date</span>")
        else
            widget:set_markup(string.format("<span foreground='#a6e3a1'>%s</span>", stdout))
            widget:buttons(flatpaks_buttons)
        end
    end)

flatpaks_text = wibox.widget({
        widget = wibox.widget.textbox,
        markup = "<span foreground='#a6e3a1'></span>",
        font = beautiful.icons_font,
        buttons = flatpaks_buttons,
    })


-- Clock
clock_buttons = awful.button({ }, 1, function () awful.spawn(clock_app) end)

clock = wibox.widget({
		widget = wibox.widget.textclock,
        format = "<span foreground='#f38ba8'>%H:%M:%S</span>",
        refresh = 1,
        buttons = clock_buttons,
	})

clock_text = wibox.widget({
        widget = wibox.widget.textbox,
        markup = "<span foreground='#f38ba8'></span>",
        font = beautiful.icons_font,
        buttons = clock_buttons,
    })


-- Calendar
calendar_buttons = awful.button({ }, 1, function () awful.spawn(calendar_app) end)

calendar = wibox.widget({
		widget = wibox.widget.textclock,
        format = "<span foreground='#fab387'>%a, %d %b</span>",
        buttons = calendar_buttons,
	})

calendar_text = wibox.widget({
        widget = wibox.widget.textbox,
        markup = "<span foreground='#fab387'></span>",
        font = beautiful.icons_font,
        buttons = calendar_buttons,
    })


-- Spacers
myspacer = wibox.widget.textbox("  ")
myspacer_small = wibox.widget.textbox(" ")

-- Systray
systray = wibox.layout.margin(wibox.widget.systray(), 8, 8, 8, 8)

systray_layout = wibox.widget({
        layout  = wibox.layout.fixed.horizontal,
        myspacer,
        systray,
    })

systray_final = awful.widget.only_on_screen(systray_layout)

-- Create a wibox for each screen and add it
local taglist_buttons = gears.table.join(
                    awful.button({ }, 1, function(t) t:view_only() end),
                    awful.button({ modkey }, 1, function(t)
                                              if client.focus then
                                                  client.focus:move_to_tag(t)
                                              end
                                          end),
                    awful.button({ }, 3, awful.tag.viewtoggle),
                    awful.button({ modkey }, 3, function(t)
                                              if client.focus then
                                                  client.focus:toggle_tag(t)
                                              end
                                          end),
                    awful.button({ }, 4, function(t) awful.tag.viewnext(t.screen) end),
                    awful.button({ }, 5, function(t) awful.tag.viewprev(t.screen) end)
                )

local tasklist_buttons = gears.table.join(
                     awful.button({ }, 1, function (c)
                                              if c == client.focus then
                                                  c.minimized = true
                                              else
                                                  c:emit_signal(
                                                      "request::activate",
                                                      "tasklist",
                                                      {raise = true}
                                                  )
                                              end
                                          end),
                     awful.button({ }, 3, function()
                                              awful.menu.client_list({ theme = { width = 250 } })
                                          end),
                     awful.button({ }, 4, function ()
                                              awful.client.focus.byidx(1)
                                          end),
                     awful.button({ }, 5, function ()
                                              awful.client.focus.byidx(-1)
                                          end))

local function set_wallpaper_default(s)
    -- Wallpaper
    if beautiful.wallpaper then
        local wallpaper = beautiful.wallpaper
        -- If wallpaper is a function, call it with the screen
        if type(wallpaper) == "function" then
            wallpaper = wallpaper(s)
        end
        gears.wallpaper.maximized(wallpaper, s, true)
    end
end

local function set_wallpaper(s)
    local wallpaper1 = beautiful.wallpaper1
    local wallpaper2 = beautiful.wallpaper2
    gears.wallpaper.maximized(wallpaper1, 1)
    gears.wallpaper.maximized(wallpaper2, 2)
end

-- Re-set wallpaper when a screen's geometry changes (e.g. different resolution)
screen.connect_signal("property::geometry", set_wallpaper_default)

awful.screen.connect_for_each_screen(function(s)
    -- Wallpaper
    set_wallpaper(s)

    -- Each screen has its own tag table.
    local names = { "", "", "", "ﳳ", "調", "ﭮ", "阮" }
    local l = awful.layout.suit  -- Just to save some typing: use an alias.
    local layouts = { l.tile, l.tile, l.tile, l.tile, l.max, l.tile, l.tile }
    awful.tag(names, s, layouts)

    -- Create an imagebox widget which will contain an icon indicating which layout we're using.
    -- We need one layoutbox per screen.
    s.mylayoutbox = awful.widget.layoutbox(s)
    s.mylayoutbox:buttons(gears.table.join(
                           awful.button({ }, 1, function () awful.layout.inc( 1) end),
                           awful.button({ }, 3, function () awful.layout.inc(-1) end),
                           awful.button({ }, 4, function () awful.layout.inc( 1) end),
                           awful.button({ }, 5, function () awful.layout.inc(-1) end)))
    -- Add margin to layoutbox to change icon size
    layoutbox = wibox.layout.margin(s.mylayoutbox, 0, 4, 4, 4)

    -- Taglist
    s.mytaglist = awful.widget.taglist {
        screen  = s,
        filter  = awful.widget.taglist.filter.all,
        buttons = taglist_buttons
    }

    -- Tasklist
    s.mytasklist = awful.widget.tasklist {
        screen   = s,
        filter   = awful.widget.tasklist.filter.currenttags,
        buttons  = tasklist_buttons,
        widget_template = tasklist_template
    }

    -- Wibox
    s.mywibox = awful.wibar({ position = "top", screen = s, height = 32 })

    -- Add widgets to the wibox
    s.mywibox:setup {
        layout = wibox.layout.align.horizontal,
        { -- Left widgets
            layout = wibox.layout.fixed.horizontal,
            spacing = 6,

            myspacer_small,
            layoutbox,

            s.mytaglist,
            myspacer,
        },
        s.mytasklist, -- Middle widget
        { -- Right widgets
            layout = wibox.layout.fixed.horizontal,
            spacing = 6,

            systray_final,

            myspacer_small,
            packages_text,
            packages_widget,

            myspacer,
            flatpaks_text,
            flatpaks_widget,

            myspacer,
            calendar_text,
            calendar,

            myspacer,
            clock_text,
            clock,
            myspacer_small,
        },
    }
end)


-------------------
------ Mouse ------
-------------------

root.buttons(gears.table.join(
    awful.button({ }, 3, function () mymainmenu:toggle() end),
    awful.button({ }, 4, awful.tag.viewnext),
    awful.button({ }, 5, awful.tag.viewprev)
))


-------------------
--- Keybindings ---
-------------------

globalkeys = gears.table.join(
    --- Awesome ---
    awful.key({ modkey, "Control", "Shift" }, "q", awesome.quit,
              {description = "quit awesome", group = "awesome"}),

    awful.key({ modkey, "Shift"            }, "r", awesome.restart,
              {description = "reload awesome", group = "awesome"}),

    awful.key({ modkey,                    }, "s",      hotkeys_popup.show_help,
              {description = "show help", group="awesome"}),

    awful.key({ modkey,                    }, "w", function () mymainmenu:show() end,
              {description = "show menu", group = "awesome"}),


    --- Client ---
    awful.key({ modkey, "Shift" }, "j", function () awful.client.swap.byidx(  1)    end,
              {description = "swap with next client", group = "client"}),

    awful.key({ modkey, "Shift" }, "k", function () awful.client.swap.byidx( -1)    end,
              {description = "swap with previous client", group = "client"}),

    awful.key({ modkey,         }, "j",
        function ()
            awful.client.focus.byidx( 1)
        end,
        {description = "focus next client", group = "client"}),

    awful.key({ modkey,         }, "k",
        function ()
            awful.client.focus.byidx(-1)
        end,
        {description = "focus previous client", group = "client"}),

    awful.key({ modkey,         }, "u", awful.client.urgent.jumpto,
              {description = "jump to urgent client", group = "client"}),


    --- Layout ---
    awful.key({ modkey, "Shift"   }, "h",     function () awful.tag.incnmaster( 1, nil, true) end,
              {description = "increase the number of masters", group = "layout"}),

    awful.key({ modkey, "Shift"   }, "l",     function () awful.tag.incnmaster(-1, nil, true) end,
              {description = "decrease the number of masters", group = "layout"}),

    awful.key({ modkey,           }, "Tab", function () awful.layout.inc( 1)                  end,
              {description = "select next layout", group = "layout"}),

    awful.key({ modkey,           }, "h",     function () awful.tag.incmwfact(-0.05)          end,
              {description = "decrease master width", group = "layout"}),

    awful.key({ modkey,           }, "l",     function () awful.tag.incmwfact( 0.05)          end,
              {description = "increase master width", group = "layout"}),


    --- Screen ---
    awful.key({ modkey,           }, ",", function () awful.screen.focus_relative(-1) end,
              {description = "focus the previous screen", group = "screen"}),    
    
    awful.key({ modkey,           }, ".", function () awful.screen.focus_relative( 1) end,
              {description = "focus the next screen", group = "screen"}),

    awful.key({ modkey,           }, "e", function () awful.screen.focus(2)           end,
              {description = "focus screen 2", group = "screen"}),

    awful.key({ modkey,           }, "q", function () awful.screen.focus(1)           end,
              {description = "focus screen 1", group = "screen"}),


    --- State ---
    awful.key({ modkey, }, "n",
        function ()
            local c = awful.client.restore()
            -- Focus restored client
            if c then
                c:emit_signal(
                    "request::activate", "key.unminimize", {raise = true}
                )
            end
        end,
        {description = "restore minimized", group = "state"}),


    --- Tag ---
    awful.key({ modkey,           }, "Left",   awful.tag.viewprev,
              {description = "view previous", group = "tag"}),

    awful.key({ modkey,           }, "Right",  awful.tag.viewnext,
              {description = "view next", group = "tag"})
)


clientkeys = gears.table.join(
    --- Client ---
    awful.key({ modkey, "Shift" }, "Return", function (c) c:swap(awful.client.getmaster())   end,
              {description = "move to master", group = "client"}),

    awful.key({ modkey, "Shift" }, "c",      function (c) c:kill()                           end,
              {description = "close client", group = "client"}),

    awful.key({ modkey,         }, "t",      function (c) c.ontop = not c.ontop              end,
              {description = "toggle keep on top", group = "client"}),


    --- Screen ---
    awful.key({ modkey, "Shift" }, ",",      function (c) c:move_to_screen(c.screen.index-1) end,
              {description = "move to the previous screen", group = "screen"}),
    
    awful.key({ modkey, "Shift" }, ".",      function (c) c:move_to_screen(c.screen.index+1) end,
              {description = "move to the next screen", group = "screen"}),

    awful.key({ modkey, "Shift" }, "e",      function (c) c:move_to_screen(2)                end,
              {description = "move to screen 2", group = "screen"}),

    awful.key({ modkey, "Shift" }, "q",      function (c) c:move_to_screen(1)                end,
              {description = "move to screen 1", group = "screen"}),


    --- State ---
    awful.key({ modkey, "Shift" }, "f",
        function (c)
            c.fullscreen = not c.fullscreen
            c:raise()
        end,
        {description = "toggle fullscreen", group = "state"}),

    awful.key({ modkey, "Shift" }, "m",
        function (c)
            c.maximized = not c.maximized
            c:raise()
        end ,
        {description = "toggle maximize", group = "state"}),

    awful.key({ modkey, "Shift" }, "n",
        function (c)
            -- The client currently has the input focus, so it cannot be
            -- minimized, since minimized clients can't have the focus.
            c.minimized = true
        end ,
        {description = "minimize", group = "state"}),

    awful.key({ modkey,         }, "f",  awful.client.floating.toggle                            ,
              {description = "toggle floating", group = "state"})
)

-- Bind all key numbers to tags.
-- Be careful: we use keycodes to make it work on any keyboard layout.
-- This should map on the top row of your keyboard, usually 1 to 9.
for i = 1, 7 do
    globalkeys = gears.table.join(globalkeys,
        -- View tag only.
        awful.key({ modkey }, "#" .. i + 9,
                  function ()
                        local screen = awful.screen.focused()
                        local tag = screen.tags[i]
                        if tag then
                           tag:view_only()
                        end
                  end,
                  {description = "view tag #"..i, group = "tag"}),
        -- Toggle tag display.
        awful.key({ modkey, "Control" }, "#" .. i + 9,
                  function ()
                      local screen = awful.screen.focused()
                      local tag = screen.tags[i]
                      if tag then
                         awful.tag.viewtoggle(tag)
                      end
                  end,
                  {description = "toggle tag #" .. i, group = "tag"}),
        -- Move client to tag.
        awful.key({ modkey, "Shift" }, "#" .. i + 9,
                  function ()
                      if client.focus then
                          local tag = client.focus.screen.tags[i]
                          if tag then
                              client.focus:move_to_tag(tag)
                          end
                     end
                  end,
                  {description = "move focused client to tag #"..i, group = "tag"})
        -- Toggle tag on focused client.
        -- awful.key({ modkey, "Control", "Shift" }, "#" .. i + 9,
        --           function ()
        --               if client.focus then
        --                   local tag = client.focus.screen.tags[i]
        --                   if tag then
        --                       client.focus:toggle_tag(tag)
        --                   end
        --               end
        --           end,
        --           {description = "toggle focused client on tag #" .. i, group = "tag"})
    )
end

clientbuttons = gears.table.join(
    awful.button({        }, 1, function (c)
        c:emit_signal("request::activate", "mouse_click", {raise = true})
    end),
    awful.button({ modkey }, 1, function (c)
        c:emit_signal("request::activate", "mouse_click", {raise = true})
        awful.mouse.client.move(c)
    end),
    awful.button({ modkey }, 3, function (c)
        c:emit_signal("request::activate", "mouse_click", {raise = true})
        awful.mouse.client.resize(c)
    end)
)

-- Set keys
root.keys(globalkeys)


-----------------
----- Rules -----
-----------------

-- Rules to apply to new clients (through the "manage" signal).
awful.rules.rules = {
    -- All clients will match this rule.
    { rule = { },
      properties = { border_width = beautiful.border_width,
                     border_color = beautiful.border_normal,
                     focus = awful.client.focus.filter,
                     raise = true,
                     keys = clientkeys,
                     buttons = clientbuttons,
                     screen = awful.screen.preferred,
                     placement = awful.placement.centered + awful.placement.no_offscreen
      }
    },

    -- Floating clients.
    { rule_any = {
        instance = {
        },

        class = {
            "floating",
            "gnome-calendar",
            "org.gnome.clocks",
            "Pavucontrol"
        },

        -- Note that the name property shown in xprop might be set slightly after creation of the client
        -- and the name shown there might not match defined rules here.
        name = {
        },

        role = {
        }
      }, properties = { floating = true }},

    -- Groups
    { rule_any = {
        class = {
            "Code"
        }
      }, properties = { tag = "", switchtotag = true }},

    { rule_any = {
        class = {
            "firefox"
        }
      }, properties = { tag = "", switchtotag = true }},

    { rule_any = {
        class = {
            "Bitwarden"
        } 
      }, properties = { tag = "ﳳ", switchtotag = true }},

    { rule_any = {
        class = {
            "Lutris",
            "Steam"
        } 
      }, properties = { tag = "調", switchtotag = true }},

    { rule_any = { 
        class = {
            "discord"
        }
      }, properties = { tag = "ﭮ", switchtotag = true }},

    { rule_any = { 
        class = {
            "Spotify"
        }
      }, properties = { tag = "阮", switchtotag = true }},
}


-------------------
----- Signals -----
-------------------

-- Signal function to execute when a new client appears.
client.connect_signal("manage", function(c)
    -- Set the windows at the slave,
    -- i.e. put it at the end of others instead of setting it master.
    if not awesome.startup then awful.client.setslave(c) end

    if awesome.startup
      and not c.size_hints.user_position
      and not c.size_hints.program_position then
        -- Prevent clients from being unreachable after screen count changes.
        awful.placement.no_offscreen(c)
    end
end)

-- Enable sloppy focus, so that focus follows mouse.
client.connect_signal("mouse::enter", function(c)
    c:emit_signal("request::activate", "mouse_enter", {raise = false})
end)

-- Fix bar not disappearing when fullscreen client appear
client.connect_signal("property::fullscreen", function(c)
    if c.fullscreen then
        gears.timer.delayed_call(function()
            if c.valid then
                c:geometry(c.screen.geometry)
            end
        end)
    end
end)

-- Border colours
function border_color_function(c) 
    if c.ontop then
        return beautiful.border_ontop
    elseif c.maximized then
        return beautiful.border_maximized
    elseif c.floating then
        return beautiful.border_floating
    else
        return beautiful.border_focus
    end
end

client.connect_signal("unfocus", function(c)
    c.border_color = beautiful.border_normal
end)

client.connect_signal("focus", function(c)
    c.border_color = border_color_function(c)
end)

client.connect_signal("property::ontop", function(c) 
    c.border_color = border_color_function(c)
end)

client.connect_signal("property::maximized", function(c) 
    c.border_color = border_color_function(c)
end)

client.connect_signal("property::floating", function(c) 
    c.border_color = border_color_function(c)
end)


-------------------
---- Autostart ----
-------------------

awful.spawn.with_shell("~/.config/awesome/autostart.sh")
