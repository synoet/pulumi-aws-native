// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::AppSync::DomainNameApiAssociation
 */
export class DomainNameApiAssociation extends pulumi.CustomResource {
    /**
     * Get an existing DomainNameApiAssociation resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): DomainNameApiAssociation {
        return new DomainNameApiAssociation(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:appsync:DomainNameApiAssociation';

    /**
     * Returns true if the given object is an instance of DomainNameApiAssociation.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is DomainNameApiAssociation {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === DomainNameApiAssociation.__pulumiType;
    }

    public /*out*/ readonly apiAssociationIdentifier!: pulumi.Output<string>;
    public readonly apiId!: pulumi.Output<string>;
    public readonly domainName!: pulumi.Output<string>;

    /**
     * Create a DomainNameApiAssociation resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: DomainNameApiAssociationArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.apiId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'apiId'");
            }
            if ((!args || args.domainName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'domainName'");
            }
            resourceInputs["apiId"] = args ? args.apiId : undefined;
            resourceInputs["domainName"] = args ? args.domainName : undefined;
            resourceInputs["apiAssociationIdentifier"] = undefined /*out*/;
        } else {
            resourceInputs["apiAssociationIdentifier"] = undefined /*out*/;
            resourceInputs["apiId"] = undefined /*out*/;
            resourceInputs["domainName"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["domainName"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(DomainNameApiAssociation.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a DomainNameApiAssociation resource.
 */
export interface DomainNameApiAssociationArgs {
    apiId: pulumi.Input<string>;
    domainName: pulumi.Input<string>;
}
