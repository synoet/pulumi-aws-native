// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::Pinpoint::ApplicationSettings
 *
 * @deprecated ApplicationSettings is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class ApplicationSettings extends pulumi.CustomResource {
    /**
     * Get an existing ApplicationSettings resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): ApplicationSettings {
        pulumi.log.warn("ApplicationSettings is deprecated: ApplicationSettings is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new ApplicationSettings(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:pinpoint:ApplicationSettings';

    /**
     * Returns true if the given object is an instance of ApplicationSettings.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ApplicationSettings {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ApplicationSettings.__pulumiType;
    }

    public readonly applicationId!: pulumi.Output<string>;
    public readonly campaignHook!: pulumi.Output<outputs.pinpoint.ApplicationSettingsCampaignHook | undefined>;
    public readonly cloudWatchMetricsEnabled!: pulumi.Output<boolean | undefined>;
    public readonly limits!: pulumi.Output<outputs.pinpoint.ApplicationSettingsLimits | undefined>;
    public readonly quietTime!: pulumi.Output<outputs.pinpoint.ApplicationSettingsQuietTime | undefined>;

    /**
     * Create a ApplicationSettings resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated ApplicationSettings is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args: ApplicationSettingsArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("ApplicationSettings is deprecated: ApplicationSettings is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.applicationId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'applicationId'");
            }
            resourceInputs["applicationId"] = args ? args.applicationId : undefined;
            resourceInputs["campaignHook"] = args ? args.campaignHook : undefined;
            resourceInputs["cloudWatchMetricsEnabled"] = args ? args.cloudWatchMetricsEnabled : undefined;
            resourceInputs["limits"] = args ? args.limits : undefined;
            resourceInputs["quietTime"] = args ? args.quietTime : undefined;
        } else {
            resourceInputs["applicationId"] = undefined /*out*/;
            resourceInputs["campaignHook"] = undefined /*out*/;
            resourceInputs["cloudWatchMetricsEnabled"] = undefined /*out*/;
            resourceInputs["limits"] = undefined /*out*/;
            resourceInputs["quietTime"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["applicationId"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(ApplicationSettings.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a ApplicationSettings resource.
 */
export interface ApplicationSettingsArgs {
    applicationId: pulumi.Input<string>;
    campaignHook?: pulumi.Input<inputs.pinpoint.ApplicationSettingsCampaignHookArgs>;
    cloudWatchMetricsEnabled?: pulumi.Input<boolean>;
    limits?: pulumi.Input<inputs.pinpoint.ApplicationSettingsLimitsArgs>;
    quietTime?: pulumi.Input<inputs.pinpoint.ApplicationSettingsQuietTimeArgs>;
}
