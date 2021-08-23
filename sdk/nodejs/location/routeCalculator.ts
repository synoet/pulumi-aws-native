// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-routecalculator.html
 */
export class RouteCalculator extends pulumi.CustomResource {
    /**
     * Get an existing RouteCalculator resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): RouteCalculator {
        return new RouteCalculator(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:location:RouteCalculator';

    /**
     * Returns true if the given object is an instance of RouteCalculator.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is RouteCalculator {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === RouteCalculator.__pulumiType;
    }

    public /*out*/ readonly arn!: pulumi.Output<string>;
    public /*out*/ readonly calculatorArn!: pulumi.Output<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-routecalculator.html#cfn-location-routecalculator-calculatorname
     */
    public readonly calculatorName!: pulumi.Output<string>;
    public /*out*/ readonly createTime!: pulumi.Output<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-routecalculator.html#cfn-location-routecalculator-datasource
     */
    public readonly dataSource!: pulumi.Output<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-routecalculator.html#cfn-location-routecalculator-description
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-routecalculator.html#cfn-location-routecalculator-pricingplan
     */
    public readonly pricingPlan!: pulumi.Output<string>;
    public /*out*/ readonly updateTime!: pulumi.Output<string>;

    /**
     * Create a RouteCalculator resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: RouteCalculatorArgs, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.calculatorName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'calculatorName'");
            }
            if ((!args || args.dataSource === undefined) && !opts.urn) {
                throw new Error("Missing required property 'dataSource'");
            }
            if ((!args || args.pricingPlan === undefined) && !opts.urn) {
                throw new Error("Missing required property 'pricingPlan'");
            }
            inputs["calculatorName"] = args ? args.calculatorName : undefined;
            inputs["dataSource"] = args ? args.dataSource : undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["pricingPlan"] = args ? args.pricingPlan : undefined;
            inputs["arn"] = undefined /*out*/;
            inputs["calculatorArn"] = undefined /*out*/;
            inputs["createTime"] = undefined /*out*/;
            inputs["updateTime"] = undefined /*out*/;
        } else {
            inputs["arn"] = undefined /*out*/;
            inputs["calculatorArn"] = undefined /*out*/;
            inputs["calculatorName"] = undefined /*out*/;
            inputs["createTime"] = undefined /*out*/;
            inputs["dataSource"] = undefined /*out*/;
            inputs["description"] = undefined /*out*/;
            inputs["pricingPlan"] = undefined /*out*/;
            inputs["updateTime"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(RouteCalculator.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a RouteCalculator resource.
 */
export interface RouteCalculatorArgs {
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-routecalculator.html#cfn-location-routecalculator-calculatorname
     */
    calculatorName: pulumi.Input<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-routecalculator.html#cfn-location-routecalculator-datasource
     */
    dataSource: pulumi.Input<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-routecalculator.html#cfn-location-routecalculator-description
     */
    description?: pulumi.Input<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-location-routecalculator.html#cfn-location-routecalculator-pricingplan
     */
    pricingPlan: pulumi.Input<string>;
}
