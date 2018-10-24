# -*- coding: utf-8 -*-
# https://www.apache.org/licenses/LICENSE-2.0.html

from abc import ABCMeta, abstractmethod
import traceback

from mod_recent_stat_logging import logError


class StatProvider:
    __metaclass__ = ABCMeta

    def getStatistics(self, region, nickname, playerId):
        # type: (str, str, str) -> dict
        try:
            return self._getStatistics(region, nickname, playerId)
        except BaseException:
            logError("Error in getStatistics(%s, %s, %s)" % (region, nickname, playerId), traceback.format_exc())
            return dict()

    @abstractmethod
    def _getStatistics(self, region, nickname, playerId):
        # type: (str, str, str) -> dict
        pass
