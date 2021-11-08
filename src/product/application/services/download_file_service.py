import requests


class DownloadReadFileService:

    def download_read_file(
        self,
        url: str,
    ) -> str:
        """
        Download and read a file from URL.

        :param url: URL of the file
        :return: text
        """
        file = requests.get(url=url)
        return file.text
