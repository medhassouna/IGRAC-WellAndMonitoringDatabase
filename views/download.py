from django.views.generic.list import ListView
from gwml2.models.download_session import DownloadSessionUser


class DownloadListView(ListView):
    model = DownloadSessionUser
    template_name = 'download/list.html'

    def get_queryset(self):
        queryset = super(DownloadListView, self).get_queryset()
        queryset = queryset.filter(user=self.request.user.id).order_by('-session__start_at')
        return queryset
