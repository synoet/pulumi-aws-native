// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package location

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Definition of AWS::Location::GeofenceCollection Resource Type
type GeofenceCollection struct {
	pulumi.CustomResourceState

	Arn                   pulumi.StringOutput                    `pulumi:"arn"`
	CollectionArn         pulumi.StringOutput                    `pulumi:"collectionArn"`
	CollectionName        pulumi.StringOutput                    `pulumi:"collectionName"`
	CreateTime            pulumi.StringOutput                    `pulumi:"createTime"`
	Description           pulumi.StringPtrOutput                 `pulumi:"description"`
	KmsKeyId              pulumi.StringPtrOutput                 `pulumi:"kmsKeyId"`
	PricingPlan           GeofenceCollectionPricingPlanPtrOutput `pulumi:"pricingPlan"`
	PricingPlanDataSource pulumi.StringPtrOutput                 `pulumi:"pricingPlanDataSource"`
	UpdateTime            pulumi.StringOutput                    `pulumi:"updateTime"`
}

// NewGeofenceCollection registers a new resource with the given unique name, arguments, and options.
func NewGeofenceCollection(ctx *pulumi.Context,
	name string, args *GeofenceCollectionArgs, opts ...pulumi.ResourceOption) (*GeofenceCollection, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.CollectionName == nil {
		return nil, errors.New("invalid value for required argument 'CollectionName'")
	}
	var resource GeofenceCollection
	err := ctx.RegisterResource("aws-native:location:GeofenceCollection", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetGeofenceCollection gets an existing GeofenceCollection resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetGeofenceCollection(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *GeofenceCollectionState, opts ...pulumi.ResourceOption) (*GeofenceCollection, error) {
	var resource GeofenceCollection
	err := ctx.ReadResource("aws-native:location:GeofenceCollection", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering GeofenceCollection resources.
type geofenceCollectionState struct {
}

type GeofenceCollectionState struct {
}

func (GeofenceCollectionState) ElementType() reflect.Type {
	return reflect.TypeOf((*geofenceCollectionState)(nil)).Elem()
}

type geofenceCollectionArgs struct {
	CollectionName        string                         `pulumi:"collectionName"`
	Description           *string                        `pulumi:"description"`
	KmsKeyId              *string                        `pulumi:"kmsKeyId"`
	PricingPlan           *GeofenceCollectionPricingPlan `pulumi:"pricingPlan"`
	PricingPlanDataSource *string                        `pulumi:"pricingPlanDataSource"`
}

// The set of arguments for constructing a GeofenceCollection resource.
type GeofenceCollectionArgs struct {
	CollectionName        pulumi.StringInput
	Description           pulumi.StringPtrInput
	KmsKeyId              pulumi.StringPtrInput
	PricingPlan           GeofenceCollectionPricingPlanPtrInput
	PricingPlanDataSource pulumi.StringPtrInput
}

func (GeofenceCollectionArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*geofenceCollectionArgs)(nil)).Elem()
}

type GeofenceCollectionInput interface {
	pulumi.Input

	ToGeofenceCollectionOutput() GeofenceCollectionOutput
	ToGeofenceCollectionOutputWithContext(ctx context.Context) GeofenceCollectionOutput
}

func (*GeofenceCollection) ElementType() reflect.Type {
	return reflect.TypeOf((**GeofenceCollection)(nil)).Elem()
}

func (i *GeofenceCollection) ToGeofenceCollectionOutput() GeofenceCollectionOutput {
	return i.ToGeofenceCollectionOutputWithContext(context.Background())
}

func (i *GeofenceCollection) ToGeofenceCollectionOutputWithContext(ctx context.Context) GeofenceCollectionOutput {
	return pulumi.ToOutputWithContext(ctx, i).(GeofenceCollectionOutput)
}

type GeofenceCollectionOutput struct{ *pulumi.OutputState }

func (GeofenceCollectionOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**GeofenceCollection)(nil)).Elem()
}

func (o GeofenceCollectionOutput) ToGeofenceCollectionOutput() GeofenceCollectionOutput {
	return o
}

func (o GeofenceCollectionOutput) ToGeofenceCollectionOutputWithContext(ctx context.Context) GeofenceCollectionOutput {
	return o
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*GeofenceCollectionInput)(nil)).Elem(), &GeofenceCollection{})
	pulumi.RegisterOutputType(GeofenceCollectionOutput{})
}
