import wx

#file selector dialog
def get_path(string, search, wildcard):
    app = wx.App(None)
    style = wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
    dialog = wx.FileDialog(None, string, defaultDir=search, wildcard=wildcard, style=style)
    if dialog.ShowModal() == wx.ID_OK:
        path = dialog.GetPath()
    else:
        path = None
    dialog.Destroy()
    return path


def get_path_new(string, search, wildcard):
    app = wx.App(None)
    style = wx.FD_OPEN
    dialog = wx.FileDialog(None, string, defaultDir=search, wildcard=wildcard, style=style)
    if dialog.ShowModal() == wx.ID_OK:
        path = dialog.GetPath()
    else:
        path = None
    dialog.Destroy()
    return path