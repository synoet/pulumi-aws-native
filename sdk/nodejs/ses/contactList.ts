// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource schema for AWS::SES::ContactList.
 */
export class ContactList extends pulumi.CustomResource {
    /**
     * Get an existing ContactList resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): ContactList {
        return new ContactList(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:ses:ContactList';

    /**
     * Returns true if the given object is an instance of ContactList.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ContactList {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ContactList.__pulumiType;
    }

    /**
     * The name of the contact list.
     */
    public readonly contactListName!: pulumi.Output<string | undefined>;
    /**
     * The description of the contact list.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * The tags (keys and values) associated with the contact list.
     */
    public readonly tags!: pulumi.Output<outputs.ses.ContactListTag[] | undefined>;
    /**
     * The topics associated with the contact list.
     */
    public readonly topics!: pulumi.Output<outputs.ses.ContactListTopic[] | undefined>;

    /**
     * Create a ContactList resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: ContactListArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            resourceInputs["contactListName"] = args ? args.contactListName : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["topics"] = args ? args.topics : undefined;
        } else {
            resourceInputs["contactListName"] = undefined /*out*/;
            resourceInputs["description"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["topics"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(ContactList.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a ContactList resource.
 */
export interface ContactListArgs {
    /**
     * The name of the contact list.
     */
    contactListName?: pulumi.Input<string>;
    /**
     * The description of the contact list.
     */
    description?: pulumi.Input<string>;
    /**
     * The tags (keys and values) associated with the contact list.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.ses.ContactListTagArgs>[]>;
    /**
     * The topics associated with the contact list.
     */
    topics?: pulumi.Input<pulumi.Input<inputs.ses.ContactListTopicArgs>[]>;
}
