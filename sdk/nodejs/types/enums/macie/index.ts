// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***


export const FindingsFilterFindingFilterAction = {
    Archive: "ARCHIVE",
    Noop: "NOOP",
} as const;

export type FindingsFilterFindingFilterAction = (typeof FindingsFilterFindingFilterAction)[keyof typeof FindingsFilterFindingFilterAction];

export const SessionFindingPublishingFrequency = {
    FifteenMinutes: "FIFTEEN_MINUTES",
    OneHour: "ONE_HOUR",
    SixHours: "SIX_HOURS",
} as const;

/**
 * A enumeration value that specifies how frequently finding updates are published.
 */
export type SessionFindingPublishingFrequency = (typeof SessionFindingPublishingFrequency)[keyof typeof SessionFindingPublishingFrequency];

export const SessionStatus = {
    Enabled: "ENABLED",
    Paused: "PAUSED",
} as const;

/**
 * A enumeration value that specifies the status of the Macie Session.
 */
export type SessionStatus = (typeof SessionStatus)[keyof typeof SessionStatus];
