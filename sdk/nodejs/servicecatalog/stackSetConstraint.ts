// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::ServiceCatalog::StackSetConstraint
 *
 * @deprecated StackSetConstraint is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class StackSetConstraint extends pulumi.CustomResource {
    /**
     * Get an existing StackSetConstraint resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): StackSetConstraint {
        pulumi.log.warn("StackSetConstraint is deprecated: StackSetConstraint is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new StackSetConstraint(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:servicecatalog:StackSetConstraint';

    /**
     * Returns true if the given object is an instance of StackSetConstraint.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is StackSetConstraint {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === StackSetConstraint.__pulumiType;
    }

    public readonly acceptLanguage!: pulumi.Output<string | undefined>;
    public readonly accountList!: pulumi.Output<string[]>;
    public readonly adminRole!: pulumi.Output<string>;
    public readonly description!: pulumi.Output<string>;
    public readonly executionRole!: pulumi.Output<string>;
    public readonly portfolioId!: pulumi.Output<string>;
    public readonly productId!: pulumi.Output<string>;
    public readonly regionList!: pulumi.Output<string[]>;
    public readonly stackInstanceControl!: pulumi.Output<string>;

    /**
     * Create a StackSetConstraint resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated StackSetConstraint is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args: StackSetConstraintArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("StackSetConstraint is deprecated: StackSetConstraint is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.accountList === undefined) && !opts.urn) {
                throw new Error("Missing required property 'accountList'");
            }
            if ((!args || args.adminRole === undefined) && !opts.urn) {
                throw new Error("Missing required property 'adminRole'");
            }
            if ((!args || args.description === undefined) && !opts.urn) {
                throw new Error("Missing required property 'description'");
            }
            if ((!args || args.executionRole === undefined) && !opts.urn) {
                throw new Error("Missing required property 'executionRole'");
            }
            if ((!args || args.portfolioId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'portfolioId'");
            }
            if ((!args || args.productId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'productId'");
            }
            if ((!args || args.regionList === undefined) && !opts.urn) {
                throw new Error("Missing required property 'regionList'");
            }
            if ((!args || args.stackInstanceControl === undefined) && !opts.urn) {
                throw new Error("Missing required property 'stackInstanceControl'");
            }
            resourceInputs["acceptLanguage"] = args ? args.acceptLanguage : undefined;
            resourceInputs["accountList"] = args ? args.accountList : undefined;
            resourceInputs["adminRole"] = args ? args.adminRole : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["executionRole"] = args ? args.executionRole : undefined;
            resourceInputs["portfolioId"] = args ? args.portfolioId : undefined;
            resourceInputs["productId"] = args ? args.productId : undefined;
            resourceInputs["regionList"] = args ? args.regionList : undefined;
            resourceInputs["stackInstanceControl"] = args ? args.stackInstanceControl : undefined;
        } else {
            resourceInputs["acceptLanguage"] = undefined /*out*/;
            resourceInputs["accountList"] = undefined /*out*/;
            resourceInputs["adminRole"] = undefined /*out*/;
            resourceInputs["description"] = undefined /*out*/;
            resourceInputs["executionRole"] = undefined /*out*/;
            resourceInputs["portfolioId"] = undefined /*out*/;
            resourceInputs["productId"] = undefined /*out*/;
            resourceInputs["regionList"] = undefined /*out*/;
            resourceInputs["stackInstanceControl"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["portfolioId", "productId"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(StackSetConstraint.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a StackSetConstraint resource.
 */
export interface StackSetConstraintArgs {
    acceptLanguage?: pulumi.Input<string>;
    accountList: pulumi.Input<pulumi.Input<string>[]>;
    adminRole: pulumi.Input<string>;
    description: pulumi.Input<string>;
    executionRole: pulumi.Input<string>;
    portfolioId: pulumi.Input<string>;
    productId: pulumi.Input<string>;
    regionList: pulumi.Input<pulumi.Input<string>[]>;
    stackInstanceControl: pulumi.Input<string>;
}
