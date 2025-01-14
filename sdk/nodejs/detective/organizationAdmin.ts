// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Resource schema for AWS::Detective::OrganizationAdmin
 */
export class OrganizationAdmin extends pulumi.CustomResource {
    /**
     * Get an existing OrganizationAdmin resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): OrganizationAdmin {
        return new OrganizationAdmin(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:detective:OrganizationAdmin';

    /**
     * Returns true if the given object is an instance of OrganizationAdmin.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is OrganizationAdmin {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === OrganizationAdmin.__pulumiType;
    }

    /**
     * The account ID of the account that should be registered as your Organization's delegated administrator for Detective
     */
    public readonly accountId!: pulumi.Output<string>;
    /**
     * The Detective graph ARN
     */
    public /*out*/ readonly graphArn!: pulumi.Output<string>;

    /**
     * Create a OrganizationAdmin resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: OrganizationAdminArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.accountId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'accountId'");
            }
            resourceInputs["accountId"] = args ? args.accountId : undefined;
            resourceInputs["graphArn"] = undefined /*out*/;
        } else {
            resourceInputs["accountId"] = undefined /*out*/;
            resourceInputs["graphArn"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["accountId"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(OrganizationAdmin.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a OrganizationAdmin resource.
 */
export interface OrganizationAdminArgs {
    /**
     * The account ID of the account that should be registered as your Organization's delegated administrator for Detective
     */
    accountId: pulumi.Input<string>;
}
