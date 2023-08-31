// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::SSMContacts::ContactChannel
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

    /**
     * The Amazon Resource Name (ARN) of the engagement to a contact channel.
     */
    public /*out*/ readonly arn!: pulumi.Output<string>;
    /**
     * The details that SSM Incident Manager uses when trying to engage the contact channel.
     */
    public readonly channelAddress!: pulumi.Output<string | undefined>;
    /**
     * The device name. String of 6 to 50 alphabetical, numeric, dash, and underscore characters.
     */
    public readonly channelName!: pulumi.Output<string | undefined>;
    /**
     * Device type, which specify notification channel. Currently supported values: “SMS”, “VOICE”, “EMAIL”, “CHATBOT.
     */
    public readonly channelType!: pulumi.Output<enums.ssmcontacts.ContactChannelChannelType | undefined>;
    /**
     * ARN of the contact resource
     */
    public readonly contactId!: pulumi.Output<string | undefined>;
    /**
     * If you want to activate the channel at a later time, you can choose to defer activation. SSM Incident Manager can't engage your contact channel until it has been activated.
     */
    public readonly deferActivation!: pulumi.Output<boolean | undefined>;

    /**
     * Create a ContactChannel resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: ContactChannelArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            resourceInputs["channelAddress"] = args ? args.channelAddress : undefined;
            resourceInputs["channelName"] = args ? args.channelName : undefined;
            resourceInputs["channelType"] = args ? args.channelType : undefined;
            resourceInputs["contactId"] = args ? args.contactId : undefined;
            resourceInputs["deferActivation"] = args ? args.deferActivation : undefined;
            resourceInputs["arn"] = undefined /*out*/;
        } else {
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["channelAddress"] = undefined /*out*/;
            resourceInputs["channelName"] = undefined /*out*/;
            resourceInputs["channelType"] = undefined /*out*/;
            resourceInputs["contactId"] = undefined /*out*/;
            resourceInputs["deferActivation"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["channelType", "contactId"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(ContactChannel.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a ContactChannel resource.
 */
export interface ContactChannelArgs {
    /**
     * The details that SSM Incident Manager uses when trying to engage the contact channel.
     */
    channelAddress?: pulumi.Input<string>;
    /**
     * The device name. String of 6 to 50 alphabetical, numeric, dash, and underscore characters.
     */
    channelName?: pulumi.Input<string>;
    /**
     * Device type, which specify notification channel. Currently supported values: “SMS”, “VOICE”, “EMAIL”, “CHATBOT.
     */
    channelType?: pulumi.Input<enums.ssmcontacts.ContactChannelChannelType>;
    /**
     * ARN of the contact resource
     */
    contactId?: pulumi.Input<string>;
    /**
     * If you want to activate the channel at a later time, you can choose to defer activation. SSM Incident Manager can't engage your contact channel until it has been activated.
     */
    deferActivation?: pulumi.Input<boolean>;
}
