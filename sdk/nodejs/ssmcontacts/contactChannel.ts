// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-contactchannel.html
 */
export class ContactChannel extends pulumi.CustomResource {
    /**
     * Get an existing ContactChannel resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): ContactChannel {
        return new ContactChannel(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:ssmcontacts:ContactChannel';

    /**
     * Returns true if the given object is an instance of ContactChannel.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ContactChannel {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ContactChannel.__pulumiType;
    }

    public /*out*/ readonly arn!: pulumi.Output<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-contactchannel.html#cfn-ssmcontacts-contactchannel-channeladdress
     */
    public readonly channelAddress!: pulumi.Output<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-contactchannel.html#cfn-ssmcontacts-contactchannel-channelname
     */
    public readonly channelName!: pulumi.Output<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-contactchannel.html#cfn-ssmcontacts-contactchannel-channeltype
     */
    public readonly channelType!: pulumi.Output<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-contactchannel.html#cfn-ssmcontacts-contactchannel-contactid
     */
    public readonly contactId!: pulumi.Output<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-contactchannel.html#cfn-ssmcontacts-contactchannel-deferactivation
     */
    public readonly deferActivation!: pulumi.Output<boolean | undefined>;

    /**
     * Create a ContactChannel resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ContactChannelArgs, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.channelAddress === undefined) && !opts.urn) {
                throw new Error("Missing required property 'channelAddress'");
            }
            if ((!args || args.channelName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'channelName'");
            }
            if ((!args || args.channelType === undefined) && !opts.urn) {
                throw new Error("Missing required property 'channelType'");
            }
            if ((!args || args.contactId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'contactId'");
            }
            inputs["channelAddress"] = args ? args.channelAddress : undefined;
            inputs["channelName"] = args ? args.channelName : undefined;
            inputs["channelType"] = args ? args.channelType : undefined;
            inputs["contactId"] = args ? args.contactId : undefined;
            inputs["deferActivation"] = args ? args.deferActivation : undefined;
            inputs["arn"] = undefined /*out*/;
        } else {
            inputs["arn"] = undefined /*out*/;
            inputs["channelAddress"] = undefined /*out*/;
            inputs["channelName"] = undefined /*out*/;
            inputs["channelType"] = undefined /*out*/;
            inputs["contactId"] = undefined /*out*/;
            inputs["deferActivation"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(ContactChannel.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a ContactChannel resource.
 */
export interface ContactChannelArgs {
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-contactchannel.html#cfn-ssmcontacts-contactchannel-channeladdress
     */
    channelAddress: pulumi.Input<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-contactchannel.html#cfn-ssmcontacts-contactchannel-channelname
     */
    channelName: pulumi.Input<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-contactchannel.html#cfn-ssmcontacts-contactchannel-channeltype
     */
    channelType: pulumi.Input<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-contactchannel.html#cfn-ssmcontacts-contactchannel-contactid
     */
    contactId: pulumi.Input<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-contactchannel.html#cfn-ssmcontacts-contactchannel-deferactivation
     */
    deferActivation?: pulumi.Input<boolean>;
}
