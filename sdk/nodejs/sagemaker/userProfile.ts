// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::SageMaker::UserProfile
 */
export class UserProfile extends pulumi.CustomResource {
    /**
     * Get an existing UserProfile resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): UserProfile {
        return new UserProfile(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:sagemaker:UserProfile';

    /**
     * Returns true if the given object is an instance of UserProfile.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is UserProfile {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === UserProfile.__pulumiType;
    }

    /**
     * The ID of the associated Domain.
     */
    public readonly domainId!: pulumi.Output<string>;
    /**
     * A specifier for the type of value specified in SingleSignOnUserValue. Currently, the only supported value is "UserName". If the Domain's AuthMode is SSO, this field is required. If the Domain's AuthMode is not SSO, this field cannot be specified.
     */
    public readonly singleSignOnUserIdentifier!: pulumi.Output<string | undefined>;
    /**
     * The username of the associated AWS Single Sign-On User for this UserProfile. If the Domain's AuthMode is SSO, this field is required, and must match a valid username of a user in your directory. If the Domain's AuthMode is not SSO, this field cannot be specified.
     */
    public readonly singleSignOnUserValue!: pulumi.Output<string | undefined>;
    /**
     * A list of tags to apply to the user profile.
     */
    public readonly tags!: pulumi.Output<outputs.sagemaker.UserProfileTag[] | undefined>;
    /**
     * The user profile Amazon Resource Name (ARN).
     */
    public /*out*/ readonly userProfileArn!: pulumi.Output<string>;
    /**
     * A name for the UserProfile.
     */
    public readonly userProfileName!: pulumi.Output<string>;
    /**
     * A collection of settings.
     */
    public readonly userSettings!: pulumi.Output<outputs.sagemaker.UserProfileUserSettings | undefined>;

    /**
     * Create a UserProfile resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: UserProfileArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.domainId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'domainId'");
            }
            resourceInputs["domainId"] = args ? args.domainId : undefined;
            resourceInputs["singleSignOnUserIdentifier"] = args ? args.singleSignOnUserIdentifier : undefined;
            resourceInputs["singleSignOnUserValue"] = args ? args.singleSignOnUserValue : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["userProfileName"] = args ? args.userProfileName : undefined;
            resourceInputs["userSettings"] = args ? args.userSettings : undefined;
            resourceInputs["userProfileArn"] = undefined /*out*/;
        } else {
            resourceInputs["domainId"] = undefined /*out*/;
            resourceInputs["singleSignOnUserIdentifier"] = undefined /*out*/;
            resourceInputs["singleSignOnUserValue"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["userProfileArn"] = undefined /*out*/;
            resourceInputs["userProfileName"] = undefined /*out*/;
            resourceInputs["userSettings"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["domainId", "singleSignOnUserIdentifier", "singleSignOnUserValue", "tags[*]", "userProfileName", "userSettings.rStudioServerProAppSettings.accessStatus", "userSettings.rStudioServerProAppSettings.userGroup"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(UserProfile.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a UserProfile resource.
 */
export interface UserProfileArgs {
    /**
     * The ID of the associated Domain.
     */
    domainId: pulumi.Input<string>;
    /**
     * A specifier for the type of value specified in SingleSignOnUserValue. Currently, the only supported value is "UserName". If the Domain's AuthMode is SSO, this field is required. If the Domain's AuthMode is not SSO, this field cannot be specified.
     */
    singleSignOnUserIdentifier?: pulumi.Input<string>;
    /**
     * The username of the associated AWS Single Sign-On User for this UserProfile. If the Domain's AuthMode is SSO, this field is required, and must match a valid username of a user in your directory. If the Domain's AuthMode is not SSO, this field cannot be specified.
     */
    singleSignOnUserValue?: pulumi.Input<string>;
    /**
     * A list of tags to apply to the user profile.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.sagemaker.UserProfileTagArgs>[]>;
    /**
     * A name for the UserProfile.
     */
    userProfileName?: pulumi.Input<string>;
    /**
     * A collection of settings.
     */
    userSettings?: pulumi.Input<inputs.sagemaker.UserProfileUserSettingsArgs>;
}
